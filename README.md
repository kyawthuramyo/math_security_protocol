# Mathematical Security Protocol (v5)

A high-security, layered cryptographic protocol designed for hackathons, featuring robust multi-stage encryption, prime-indexed decoy injection, and dual-side packet validation to prevent tampering, injection, and drop attacks.

---

## 🛡️ Architecture & Pipeline (10-Step Flow)

### [SENDER SIDE]
1. **Chunker**: Splits raw plaintext into low-level byte chunks (`chunker.py`).
2. **Local Forward Transformation**: Applies coordinate confusion to individual chunks (`localforwardtransformer.py`).
3. **Global Forward Transformation**: Shuffles chunks using prime-weight distribution (`globalforwardtransformer.py`).
4. **Decoy Injection**: Injects dummy decoy chunks into non-prime indices within a 1,000-cycle limit (`decoy_injector.py`).
5. **Sender Validation**: Pre-checks outgoing mixed stream and metadata count to ensure structural integrity before dispatch (`sender_validator.py`).

### [RECEIVER SIDE]
6. **Receiver Validation**: Pre-checks incoming packet counts against the strict 1,000-cycle limit to detect drop/injection attacks (`receiver_validator.py`).
7. **Decoy Filtering**: Discards non-prime decoy packets, extracting only authentic chunks (`decoy_filter.py`).
8. **Global Reverse Transformation**: Un-shuffles chunks back to their original sequence using prime weights (`globalreversetransformer.py`).
9. **Local Reverse Transformation**: Deciphers byte values to restore original states (`localreversetransformer.py`).
10. **Combiner**: Rebuilds the decrypted byte chunks back into the original plaintext string (`combiner.py`).

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.

### Running the Protocol
Clone the repository and run the main execution script:

```bash
git clone [https://github.com/kyawthuramyo/math_security_protocol.git](https://github.com/kyawthuramyo/math_security_protocol.git)
cd math_security_protocol
python main.py