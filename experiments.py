"""
Expreriments Plan for Matrix Encryption Walk.
This script runs a series of experiments on the MEW encryption scheme.
## Expreriment Goals
- Evaluate the security and performance of our MEW implementation.
- Test encryption/decryption correctness for various plaintexts and key sizes.
- Measure speed and memory usage for different message lengths.
- Optionally, analyze resistance to simple attacks (e.g., avalanche effect, key sensitivity).
## Experimental Variables
- Key size: Try different matrix sizes (e.g., 8x8, 16x16, 32x32, 64x64).
- Plaintext length: Short, medium, and long messages.
- Random keys: Use multiple random seeds for key generation.
## Metrics to Collect
- Encryption and decryption time.
- Ciphertext length vs. plaintext length.
- Success/failure of decryption (does output match input?).
- (Optional) Bit-flip/avalanche effect: How much does ciphertext change if you flip one bit in plaintext or key?
## Experiment Script Structure
Loop over key sizes and plaintexts.
For each, generate random keys, encrypt, decrypt, and record results.
Print or save results in a table or CSV for analysis.
"""