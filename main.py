from core.Encryption.chunker import DataChunker
from core.Encryption.localforwardtransformer import LocalForwardTransformer
from core.Decryption.localreversetransformer import LocalReverseTransformer
from core.Decryption.combiner import DataCombiner

def main():
    print("=" * 65)
    print("      MATH FOR SYSTEMS SECURITY: MODULE 1 PIPELINE TEST")
    print("=" * 65)
    
    # 1. Request user input / User ထံမှ စာသားတောင်းခံခြင်း
    user_input = input("\n> Enter your secret text to encrypt/chunk: ")
    
    if not user_input.strip():
        print("[-] Error: Input cannot be empty! (ထည့်သွင်းထားသော စာသား မရှိပါ)")
        return

    # Set chunk size / Chunk အရွယ်အစား သတ်မှတ်ခြင်း (ဥပမာ - ၁၂ လုံး)
    chunk_size = 12
    print(f"\n[+] Processing with chunk size = {chunk_size}...")

    # 2. Step 1: Chunker Module (Convert text to low-level chunks)
    # စာသားကို Chunker ဖြင့် အပိုင်းငယ်များ (Low-level integer arrays) ခွဲထုတ်ခြင်း
    chunker = DataChunker(chunk_size=chunk_size)
    low_level_chunks = chunker.text_to_low_level_chunks(user_input)
    
    print(f"\n[STEP 1 - SUCCESS] Chunker generated {len(low_level_chunks)} chunks successfully.")
    for idx, chunk in enumerate(low_level_chunks):
        print(f"  -> Chunk {idx + 1}: {chunk}")

    # 3. Step 2: Local Forward Transformer Module (Encryption)
    # Forward Transformer ဖြင့် ဒေတာများကို နေရာအလိုက် ဝှက်ပေးခြင်း (Encryption)
    forward_transformer = LocalForwardTransformer(chunk_size=chunk_size)
    encrypted_chunks = forward_transformer.transform_chunks(low_level_chunks)
    
    print(f"\n[STEP 2 - SUCCESS] Local Forward Transformation (Encryption) completed.")
    for idx, chunk in enumerate(encrypted_chunks):
        print(f"  -> Encrypted Chunk {idx + 1}: {chunk}")

    # 4. Step 3: Local Reverse Transformer Module (Decryption)
    # Reverse Transformer ဖြင့် ဝှက်ထားသည်များကို မူလတန်ဖိုးသို့ ပြန်ဖော်ခြင်း (Decryption)
    reverse_transformer = LocalReverseTransformer(chunk_size=chunk_size)
    decrypted_chunks = reverse_transformer.reverse_chunks(encrypted_chunks)
    
    print(f"\n[STEP 3 - SUCCESS] Local Reverse Transformation (Decryption) completed.")
    for idx, chunk in enumerate(decrypted_chunks):
        print(f"  -> Restored Chunk {idx + 1}: {chunk}")

    # 5. Step 4: Combiner Module (Restore back to plaintext)
    # Combiner ဖြင့် Chunk များကို ပြန်လည်စုစည်းပြီး မူလစာသားအဖြစ် ပြောင်းလဲခြင်း
    combiner = DataCombiner()
    restored_text = combiner.combine_and_restore(decrypted_chunks)
    
    print("\n" + "=" * 65)
    print(f"[STEP 4 - SUCCESS] Combiner successfully restored the text!")
    print(f"[*] Original Text : {user_input}")
    print(f"[*] Restored Text : {restored_text}")
    print("=" * 65)
    
    # Final Verification / အမှန်ကန်ဆုံး ဟုတ်မဟုတ် စစ်ဆေးခြင်း
    if user_input == restored_text:
        print("\nSUCCESS: The entire Local Pipeline verified perfectly!")
    else:
        print("\nFAILURE: Restored text does not match original text.")

if __name__ == "__main__":
    main()