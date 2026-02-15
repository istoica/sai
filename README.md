# sai
Scratchpad for AI driven projects

## Rust Sorting Program

This project now includes a Rust version of the sorting program from `sort.py`.

## Files

- `Cargo.toml`: Rust project configuration
- `src/main.rs`: Rust implementation of the sorter
- `sort.py`: original Python version (kept for reference)

## 1. Install Rust (first-time setup)

On macOS/Linux:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Then reload your shell:

```bash
source "$HOME/.cargo/env"
```

Confirm it worked:

```bash
cargo --version
rustc --version
```

## 2. Run the Rust program

From this project directory:

### Sort numbers from command line

```bash
cargo run -- 5 2 8 1 9 3
```

### Sort numbers from standard input

```bash
echo "10 5 3 7 1" | cargo run
```

### Interactive mode

```bash
cargo run
# Then type numbers separated by spaces/newlines and press Ctrl+D
```

## Features

- Supports integers and floating-point numbers
- Supports negative numbers
- Uses quicksort algorithm
- Accepts input via command line arguments or standard input
