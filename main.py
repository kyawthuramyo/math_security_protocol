from core.Encryption.chunker import DataChunker
from core.Encryption.localforwardtransformer import LocalForwardTransformer
from core.Encryption.globalforwardtransformer import GlobalForwardTransformer
from core.Decryption.globalreversetransformer import GlobalReverseTransformer
from core.Decryption.localreversetransformer import LocalReverseTransformer
from core.Decryption.combiner import DataCombiner

def main():
    print("=" * 65)
    print("   MATH FOR SYSTEMS SECURITY: LAYERED PIPELINE TEST")
    print("=" * 65)
    
    # 1. Request user input / User ထံမှ စာသားတောင်းခံခြင်း
    user_input = input("\n> Enter your secret text to encrypt/chunk: ")
    
    if not user_input.strip():
        print("[-] Error: Input cannot be empty! (ထည့်သွင်းထားသော စာသား မရှိပါ)")
        return

    # Set chunk size & batch size / Chunk နှင့် Batch အရွယ်အစား သတ်မှတ်ခြင်း
    chunk_size = 12
    batch_size = 100
    print(f"\n[+] Processing with chunk_size = {chunk_size}, batch_size = {batch_size}...")

    # 2. Step 1: Chunker Module (Convert text to low-level chunks)
    # စာသားကို Chunker ဖြင့် အပိုင်းငယ်များအဖြစ် ခွဲထုတ်ခြင်း
    chunker = DataChunker(chunk_size=chunk_size)
    low_level_chunks = chunker.text_to_low_level_chunks(user_input)
    
    print(f"\n[STEP 1 - SUCCESS] Chunker generated {len(low_level_chunks)} chunks.")
    for idx, chunk in enumerate(low_level_chunks):
        print(f"  -> Original Chunk {idx + 1}: {chunk}")

    # 3. Step 2: Local Forward Transformer Module (Local Encryption)
    # ဒုတိယအဆင့် - Local Forward ဖြင့် Chunk တစ်ခုချင်းစီ၏ အတွင်းပိုင်းတန်ဖိုးများကို အရင်ဝှက်ခြင်း (Confusion)
    local_forward = LocalForwardTransformer(chunk_size=chunk_size)
    locally_encrypted_chunks = local_forward.transform_chunks(low_level_chunks)
    
    print(f"\n[STEP 2 - SUCCESS] Local Forward Transformation (Encryption) completed.")
    for idx, chunk in enumerate(locally_encrypted_chunks):
        print(f"  -> Locally Encrypted Chunk {idx + 1}: {chunk}")

    # 4. Step 3: Global Forward Transformer Module (Global Diffusion & Shuffling)
    # တတိယအဆင့် - Global Forward ဖြင့် ဝှက်ပြီးသား Chunk များကို Prime Index များသုံး၍ အစဉ်ပြောင်းလဲရောနှောခြင်း (Diffusion)
    global_forward = GlobalForwardTransformer(batch_size=batch_size)
    fully_encrypted_chunks, shuffle_metadata = global_forward.transform_global(locally_encrypted_chunks)
    
    print(f"\n[STEP 3 - SUCCESS] Global Forward Transformation (Prime Shuffling) completed.")
    print(f"  -> Shuffle Metadata (Prime Weights): {shuffle_metadata}")
    for idx, chunk in enumerate(fully_encrypted_chunks):
        print(f"  -> Fully Encrypted & Shuffled Chunk {idx + 1}: {chunk}")

    # ==========================================
    # DECRYPTION PIPELINE (ပြန်လည်ဖော်ထုတ်ခြင်း အဆင့်များ - ပြောင်းပြန်စနစ်)
    # ==========================================

    # 5. Step 4: Global Reverse Transformer Module (Global Un-shuffling via Search & Sort)
    # ပထမအဆင့် (ပြန်ဖြည်စဉ်) - Global Reverse ဖြင့် Metadata ကိုသုံးကာ Search & Sort လုပ်၍ Chunk များကို မူလအစဉ်အတိုင်း ပြန်စီခြင်း
    global_reverse = GlobalReverseTransformer(batch_size=batch_size)
    globally_restored_chunks = global_reverse.reverse_global(fully_encrypted_chunks, shuffle_metadata)
    
    print(f"\n[STEP 4 - SUCCESS] Global Reverse Transformation (Search & Sort) completed.")
    for idx, chunk in enumerate(globally_restored_chunks):
        print(f"  -> Reordered Chunk {idx + 1}: {chunk}")

    # 6. Step 5: Local Reverse Transformer Module (Local Decryption)
    # ဒုတိယအဆင့် (ပြန်ဖြည်စဉ်) - Local Reverse ဖြင့် ဝှက်ထားသော အတွင်းပိုင်းတန်ဖိုးများကို ပြန်လည်ဖော်ထုတ်ခြင်း (Decryption)
    local_reverse = LocalReverseTransformer(chunk_size=chunk_size)
    decrypted_chunks = local_reverse.reverse_chunks(globally_restored_chunks)
    
    print(f"\n[STEP 5 - SUCCESS] Local Reverse Transformation (Decryption) completed.")
    for idx, chunk in enumerate(decrypted_chunks):
        print(f"  -> Decrypted Chunk {idx + 1}: {chunk}")

    # 7. Step 6: Combiner Module (Restore back to plaintext)
    # တတိယအဆင့် (ပြန်ဖြည်စဉ်) — Combiner ဖြင့် Chunk များကို ပြန်လည်စုစည်းပြီး မူလစာသားအဖြစ် ပြောင်းလဲခြင်း
    combiner = DataCombiner()
    restored_text = combiner.combine_and_restore(decrypted_chunks)
    
    print("\n" + "=" * 65)
    print(f"[STEP 6 - SUCCESS] Combiner successfully restored the text!")
    print(f"[*] Original Text : {user_input}")
    print(f"[*] Restored Text : {restored_text}")
    print("=" * 65)
    
    # Final Verification / အမှန်ကန်ဆုံး ဟုတ်မဟုတ် စစ်ဆေးခြင်း
    if user_input == restored_text:
        print("\nSUCCESS: The entire Layered Pipeline verified perfectly!")
    else:
        print("\nFAILURE: Restored text does not match original text.")

if __name__ == "__main__":
    main()