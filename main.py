# =====================================================================
# [EN] Main execution entry point for Mathematical Security Protocol (v4).
# [MY] သင်္ချာအခြေပြု လုံခြုံရေး ပရိုတိုကော (ဗားရှင်း ၄) ၏ ပင်မ စတင်ရေးဆွဲသည့် ဖိုင်။
# =====================================================================

import sys
from core.Encryption.chunker import Chunker
from core.Encryption.localforwardtransformer import LocalForwardTransformer
from core.Encryption.globalforwardtransformer import GlobalForwardTransformer
from core.Encryption.decoy_injector import DecoyInjector
from core.Encryption.sender_validator import SenderValidator

from core.Decryption.receiver_validator import ReceiverValidator
from core.Decryption.decoy_filter import DecoyFilter
from core.Decryption.globalreversetransformer import GlobalReverseTransformer
from core.Decryption.localreversetransformer import LocalReverseTransformer
from core.Decryption.combiner import Combiner

def main():
    print("=" * 75)
    print("      MATHEMATICAL SECURITY PROTOCOL - v4 FULL PIPELINE WITH VALIDATORS      ")
    print("=" * 75)
    
    # -----------------------------------------------------------------
    # STEP 1: User Input & Initial Setup
    # -----------------------------------------------------------------
    user_input = input("\n[INPUT] Enter secret text to encrypt: ").strip()
    if not user_input:
        user_input = "I love ko kit. He is handsome easygoing and really kind to everyone,"
        print(f"-> Using default test text: \"{user_input}\"")

    # =================================================================
    # SENDER SIDE ENCRYPTION & VALIDATION PIPELINE
    # =================================================================
    print("\n" + "=" * 75)
    print("                        SENDER SIDE PROCESSING                         ")
    print("=" * 75)

    # 1. Chunker Layer
    print("\n" + "-" * 75)
    print("[STEP 1 - ENCRYPTION] Chunking Input Text...")
    chunker = Chunker(chunk_size=12)
    original_chunks = chunker.to_chunks(user_input)
    print(f"-> Total Chunks Created: {len(original_chunks)}")
    for i, c in enumerate(original_chunks[:3], 1):
        print(f"   Chunk {i}: {c}")

    # 2. Local Forward Transformation
    print("\n" + "-" * 75)
    print("[STEP 2 - ENCRYPTION] Local Forward Transformation (Confusion)...")
    local_forward = LocalForwardTransformer(chunk_size=12)
    local_encrypted_chunks = local_forward.transform_chunks(original_chunks)
    for i, c in enumerate(local_encrypted_chunks[:3], 1):
        print(f"   Encrypted Chunk {i}: {c}")

    # 3. Global Forward Transformation
    print("\n" + "-" * 75)
    print("[STEP 3 - ENCRYPTION] Global Forward Transformation (Diffusion)...")
    global_forward = GlobalForwardTransformer(batch_size=100)
    shuffled_chunks, prime_weights = global_forward.transform_global(local_encrypted_chunks)
    print(f"-> Calculated Prime Weights Sample: {prime_weights[:5]}...")
    for i, c in enumerate(shuffled_chunks[:3], 1):
        print(f"   Shuffled Chunk {i}: {c}")

    # 4. Decoy Injection Layer (1-1000 Cycle)
    print("\n" + "-" * 75)
    print("[STEP 4 - ENCRYPTION] Decoy Injection Layer (1 to 1000 Cycle Obfuscation)...")
    injector = DecoyInjector(cycle_limit=1000)
    mixed_stream, metadata = injector.inject_decoys(shuffled_chunks)
    print(f"-> Generated Total Mixed Stream: {len(mixed_stream)} Packets ready for transmission.")
    
    real_indices = [m['index'] for m in metadata if m['is_real']][:5]
    decoy_indices = [m['index'] for m in metadata if not m['is_real']][:5]
    print(f"   First 5 Real Indices (Primes)   : {real_indices}")
    print(f"   First 5 Decoy Indices (Non-Primes): {decoy_indices}")

    # 5. Sender Validation Pre-Check (Outgoing Stream & Metadata Verification)
    print("\n" + "-" * 75)
    print("[STEP 5 - ENCRYPTION] Sender Validation (Pre-checking mixed stream before dispatch)...")
    sender_validator = SenderValidator()
    try:
        # Sender ဘက်က ပို့မည့် mixed_stream နှင့် metadata အရေအတွက်ကို စစ်ဆေးခြင်း
        if len(mixed_stream) != 1000 or len(metadata) != 1000:
            raise ValueError("Outgoing mixed stream count does not match the 1000 cycle limit!")
        print("-> [PASSED] Sender Outgoing Mixed Stream & Metadata Count Verified (1000 Packets).")
    except ValueError as e:
        print(f"-> [FAILED] {e}")
        sys.exit(1)

    # =================================================================
    # RECEIVER SIDE VALIDATION & DECRYPTION PIPELINE
    # =================================================================
    print("\n" + "=" * 75)
    print("                       RECEIVER SIDE PROCESSING                        ")
    print("=" * 75)

    # 6. Receiver Validation Pre-Check
    print("\n" + "-" * 75)
    print("[STEP 6 - DECRYPTION] Receiver Validation (Packet Count & Integrity Pre-Check)...")
    receiver_validator = ReceiverValidator(expected_cycle_limit=1000)
    try:
        receiver_validator.validate_incoming_stream(mixed_stream, metadata)
        print(f"-> [PASSED] Packet Count Verified: Exactly {len(mixed_stream)} packets received. No tampering detected.")
    except ValueError as e:
        print(f"-> [FAILED] {e}")
        sys.exit(1)

    # 7. Decoy Filtering Layer
    print("\n" + "-" * 75)
    print("[STEP 7 - DECRYPTION] Decoy Filtering (Extracting Prime Index Chunks)...")
    decoy_filter = DecoyFilter()
    filtered_chunks = decoy_filter.filter_real_chunks(mixed_stream, metadata)
    print(f"-> Successfully Filtered Real Chunks: {len(filtered_chunks)} / {len(mixed_stream)}")

    # 8. Global Reverse Transformation
    print("\n" + "-" * 75)
    print("[STEP 8 - DECRYPTION] Global Reverse Transformation (Un-shuffling)...")
    global_reverse = GlobalReverseTransformer(batch_size=100)
    reordered_chunks = global_reverse.reverse_global(filtered_chunks, prime_weights)
    for i, c in enumerate(reordered_chunks[:3], 1):
        print(f"   Reordered Chunk {i}: {c}")

    # 9. Local Reverse Transformation
    print("\n" + "-" * 75)
    print("[STEP 9 - DECRYPTION] Local Reverse Transformation (De-confusion)...")
    local_reverse = LocalReverseTransformer(chunk_size=12)
    decrypted_chunks = local_reverse.reverse_chunks(reordered_chunks)
    for i, c in enumerate(decrypted_chunks[:3], 1):
        print(f"   Decrypted Chunk {i}: {c}")

    # 10. Combiner Layer
    print("\n" + "-" * 75)
    print("[STEP 10 - DECRYPTION] Restoring Original Text via Combiner...")
    combiner = Combiner()
    restored_text = combiner.to_text(decrypted_chunks)
    
    # Final Result Verification
    print("\n" + "=" * 75)
    print(f"[+] Original Text : {user_input}")
    print(f"[+] Restored Text : {restored_text}")
    print("=" * 75)

    if user_input == restored_text:
        print("\n[SUCCESS] Version 4 Full Pipeline with Sender & Receiver Validators verified perfectly!")
    else:
        print("\n[FAILED] Mismatch found in restored text!")

if __name__ == "__main__":
    main()