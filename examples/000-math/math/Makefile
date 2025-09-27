build-release:
	cargo build --release

gen-python: build-release
	cargo run --bin uniffi-bindgen generate --library target/release/libmath.dylib --language python --out-dir python/mathlib
	cp target/release/libmath.dylib python/mathlib

generate-all: gen-python

run-python:
	cd python && python3 main.py && cd -

run-all: run-python
