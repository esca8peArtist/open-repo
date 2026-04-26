"""CLI for hardware binding operations. Used by setup wizard and systemd units."""
import sys
import json
import logging
import click
from .binding import initialize_binding, verify_binding
from .fingerprint import collect_fingerprint

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s  %(message)s",
)


@click.group()
@click.option("--debug", is_flag=True, default=False, help="Enable debug logging.")
def cli(debug: bool) -> None:
    """AgentCore hardware binding management."""
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)


@cli.command()
def init() -> None:
    """Initialize hardware binding (first boot only).

    Collects the hardware fingerprint, generates a random salt, seals
    it to the TPM, and writes the binding state to
    /etc/agentcore/binding.json.

    Exit code 0 on success, 1 on failure.
    """
    click.echo("Initializing hardware binding…")
    success = initialize_binding()
    if success:
        click.secho("Hardware binding initialized successfully.", fg="green")
        sys.exit(0)
    else:
        click.secho(
            "Hardware binding initialization failed. "
            "Check logs for details.",
            fg="red",
            err=True,
        )
        sys.exit(1)


@cli.command()
def verify() -> None:
    """Verify hardware binding.

    Confirms that the current machine's hardware fingerprint matches the
    binding state and that the TPM can unseal the salt.

    Exits 0 if valid, 1 if not. Called by agentcore.service on every boot.
    """
    click.echo("Verifying hardware binding…")
    valid = verify_binding()
    if valid:
        click.secho("Hardware binding valid.", fg="green")
        sys.exit(0)
    else:
        click.secho(
            "Hardware binding verification FAILED. "
            "This may not be the licensed hardware.",
            fg="red",
            err=True,
        )
        sys.exit(1)


@cli.command(name="fingerprint")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "json"]),
    default="text",
    show_default=True,
    help="Output format.",
)
def fingerprint_cmd(output_format: str) -> None:
    """Print hardware fingerprint.

    Collects identifiers from this machine and prints them. Used at purchase
    time to generate a license key for the Docker Compose SKU.

    Exit code 0 on success, 1 if insufficient identifiers were found.
    """
    fp = collect_fingerprint()
    if output_format == "json":
        data = {
            "tpm_ek_hash": fp.tpm_ek_hash,
            "cpu_serial": fp.cpu_serial,
            "board_uuid": fp.board_uuid,
            "mac_address": fp.mac_address,
            "sha256_fingerprint": fp.sha256_fingerprint().hex(),
            "is_valid": fp.is_valid(),
        }
        click.echo(json.dumps(data, indent=2))
    else:
        click.echo(f"TPM EK hash   : {fp.tpm_ek_hash or '(not available)'}")
        click.echo(f"CPU serial    : {fp.cpu_serial or '(not available)'}")
        click.echo(f"Board UUID    : {fp.board_uuid or '(not available)'}")
        click.echo(f"MAC address   : {fp.mac_address or '(not available)'}")
        click.echo(f"SHA-256       : {fp.sha256_fingerprint().hex()}")
        click.echo(f"Valid (≥2 IDs): {'yes' if fp.is_valid() else 'no'}")

    if not fp.is_valid():
        click.secho(
            "Warning: fewer than 2 hardware identifiers found. "
            "License binding will not be reliable.",
            fg="yellow",
            err=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    cli()
