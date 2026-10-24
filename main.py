from core.Encryption.chunker import DataChunker
from core.Decryption.combiner import DataCombiner

def main():
    print("=" * 65)
    print("   MATH FOR SYSTEMS SECURITY: MODULE 1 PIPELINE TEST")
    print("=" * 65)

    # 1. Request user input / User ထံမှ စာသားတောင်းခံခြင်း
    user_input = input("\n> Enter your secret text to encrypt/chunk: ")
    
    if not user_input.strip():
        print("[-] Error: Input cannot be empty! (ထည့်သွင်းထားသော စာသား မရှိပါ)")
        return

    # Set chunk size / Chunk အရွယ်အစား သတ်မှတ်ခြင်း (ဥပမာ - အပိုင်းတစ်ပိုင်းလျှင် စာလုံးရေ ၁၂ လုံး)
    chunk_size = 12
    
    print(f"\n[+] Processing with chunk size = {chunk_size}...")

    # 2. Use Encryption Module (Chunker) / Encryption မော်ဂျူးကို အသုံးပြုခြင်း
    chunker = DataChunker(chunk_size=chunk_size)
    low_level_chunks = chunker.text_to_low_level_chunks(user_input)

    print("\n[MODULE 1 - ENCRYPTION] Low-Level Chunks (Integer Arrays):")
    for idx, chunk in enumerate(low_level_chunks):
        print(f"  Chunk {idx + 1}: {chunk}")

    # 3. Use Decryption Module (Combiner) / Decryption မော်ဂျူးကို အသုံးပြုခြင်း
    combiner = DataCombiner()
    restored_text = combiner.combine_and_restore(low_level_chunks)

    print("\n" + "=" * 65)
    print(f"[MODULE 2 - DECRYPTION] Restored Text:\n{restored_text}")
    print("=" * 65)

    # 4. Integrity Check / ဒေတာ မှန်ကန်မှုရှိမရှိ စစ်ဆေးခြင်း
    if user_input == restored_text:
        print(">>> SUCCESS: Data integrity verified perfectly! (ဒေတာများ တိကျမှန်ကန်မှု ရှိပါသည်) <<<")
    else:
        print(">>> ERROR: Data mismatch detected! (ဒေတာ ကွာဟချက် ရှိနေပါသည်) <<<")

if __name__ == "__main__":
    main()