# =====================================================================
# [EN] Main execution entry point for Mathematical Security Protocol.
# [MY] သင်္ချာအခြေပြု လုံခြုံရေး ပရိုတိုကော၏ ပင်မ စတင်ရေးဆွဲသည့် ဖိုင်။
# =====================================================================

from core.Encryption.chunker import Chunker
from core.Encryption.localforwardtransformer import LocalForwardTransformer
from core.Encryption.globalforwardtransformer import GlobalForwardTransformer
from core.Encryption.decoy_injector import DecoyInjector

from core.Decryption.decoy_filter import DecoyFilter
from core.Decryption.globalreversetransformer import GlobalReverseTransformer
from core.Decryption.localreversetransformer import LocalReverseTransformer
from core.Decryption.combiner import Combiner

def main():
    print("=" * 75)
    print("      MATHEMATICAL SECURITY PROTOCOL - FULL LAYERED PIPELINE DEMO      ")
    print("=" * 75)
    
    # -----------------------------------------------------------------
    # STEP 1: User Input & Initial Setup
    # -----------------------------------------------------------------
    user_input = input("\n[INPUT] Enter secret text to encrypt: ").strip()
    if not user_input:
        user_input = "I love ko kit. He is handsome easygoing and really kind to everyone,"
        print(f"-> Using default test text: \"{user_input}\"")

    # -----------------------------------------------------------------
    # STEP 2: Chunker Layer
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 1 - ENCRYPTION] Chunking Input Text...")
    chunker = Chunker(chunk_size=12)
    original_chunks = chunker.to_chunks(user_input)
    print(f"-> Total Chunks Created: {len(original_chunks)}")
    for i, c in enumerate(original_chunks[:3], 1):
        print(f"   Chunk {i}: {c}")
    if len(original_chunks) > 3:
        print(f"   ... (and {len(original_chunks) - 3} more chunks)")

    # -----------------------------------------------------------------
    # STEP 3: Local Forward Transformation (Enciphering Bytes)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 2 - ENCRYPTION] Local Forward Transformation (Confusion)...")
    local_forward = LocalForwardTransformer(chunk_size=12)
    local_encrypted_chunks = local_forward.transform_chunks(original_chunks)
    for i, c in enumerate(local_encrypted_chunks[:3], 1):
        print(f"   Encrypted Chunk {i}: {c}")

    # -----------------------------------------------------------------
    # STEP 4: Global Forward Transformation (Prime-Weight Shuffling)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 3 - ENCRYPTION] Global Forward Transformation (Diffusion)...")
    global_forward = GlobalForwardTransformer(batch_size=100)
    shuffled_chunks, prime_weights = global_forward.transform_global(local_encrypted_chunks)
    print(f"-> Calculated Prime Weights Sample: {prime_weights[:5]}...")
    for i, c in enumerate(shuffled_chunks[:3], 1):
        print(f"   Shuffled Chunk {i}: {c}")

    # -----------------------------------------------------------------
    # STEP 5: Decoy Injection (1-1000 Cycle Prime Obfuscation)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 4 - ENCRYPTION] Decoy Injection Layer (1 to 1000 Cycle Obfuscation)...")
    injector = DecoyInjector(cycle_limit=1000)
    mixed_stream, metadata = injector.inject_decoys(shuffled_chunks)
    print(f"-> Generated Total Mixed Stream: {len(mixed_stream)} Packets (1000 Cycle)")
    
    real_indices = [m['index'] for m in metadata if m['is_real']][:5]
    decoy_indices = [m['index'] for m in metadata if not m['is_real']][:5]
    print(f"   First 5 Real Indices (Primes)   : {real_indices}")
    print(f"   First 5 Decoy Indices (Non-Primes): {decoy_indices}")

    # =================================================================
    # RECEIVER SIDE DECRYPTION PIPELINE
    # =================================================================
    print("\n" + "=" * 75)
    print("                     STARTING RECEIVER DECRYPTION                      ")
    print("=" * 75)

    # -----------------------------------------------------------------
    # STEP 6: Decoy Filtering Layer (Discard Fake Packets)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 5 - DECRYPTION] Decoy Filtering (Extracting Prime Index Chunks)...")
    decoy_filter = DecoyFilter()
    filtered_chunks = decoy_filter.filter_real_chunks(mixed_stream, metadata)
    print(f"-> Successfully Filtered Real Chunks: {len(filtered_chunks)} / {len(mixed_stream)}")

    # -----------------------------------------------------------------
    # STEP 7: Global Reverse Transformation (Sort Back by Prime Weights)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 6 - DECRYPTION] Global Reverse Transformation (Un-shuffling)...")
    global_reverse = GlobalReverseTransformer(batch_size=100)
    reordered_chunks = global_reverse.reverse_global(filtered_chunks, prime_weights)
    for i, c in enumerate(reordered_chunks[:3], 1):
        print(f"   Reordered Chunk {i}: {c}")

    # -----------------------------------------------------------------
    # STEP 8: Local Reverse Transformation (Deciphering Bytes)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 7 - DECRYPTION] Local Reverse Transformation (De-confusion)...")
    local_reverse = LocalReverseTransformer(chunk_size=12)
    decrypted_chunks = local_reverse.reverse_chunks(reordered_chunks)
    for i, c in enumerate(decrypted_chunks[:3], 1):
        print(f"   Decrypted Chunk {i}: {c}")

    # -----------------------------------------------------------------
    # STEP 9: Combiner Layer (Restoring Text)
    # -----------------------------------------------------------------
    print("\n" + "-" * 75)
    print("[STEP 8 - DECRYPTION] Restoring Original Text via Combiner...")
    combiner = Combiner()
    restored_text = combiner.to_text(decrypted_chunks)
    
    print("\n" + "=" * 75)
    print(f"[+] Original Text : {user_input}")
    print(f"[+] Restored Text : {restored_text}")
    print("=" * 75)

    if user_input == restored_text:
        print("\n[SUCCESS] The entire Layered Pipeline with Decoy Injection verified perfectly!")
    else:
        print("\n[FAILED] Mismatch found in restored text!")

if __name__ == "__main__":
    main()