def coordinate_encrypt(array_12: list[int]) -> list[int]:
    """
    Coordinate-based & Index-Mixing Forward Transformation (Encryption)
    - Array ၏ index တစ်ခုချင်းစီ (coordinate) အလိုက် နေရာချ၍ index-based mixing ပြုလုပ်ခြင်း။
    - ဥပမာ - အခန်း 0 တွင် zero mixing ထည့်ခြင်းနှင့် အခြား index များကို position အလိုက် တွက်ချက်ခြင်း။
    """
    encrypted = []
    for i, val in enumerate(array_12):
        # Index-mixing rule: 
        # အခန်း 0 ဆိုရင် 0 ရောမည် (zero mixing), အခြား index များအတွက် i ကို အခြေခံ၍ factor တစ်ခု ထည့်မည်။
        mix_factor = 0 if i == 0 else (i * 3) % 256
        
        # Coordinate transformation formula: (val + index + mix_factor) % 256
        transformed_val = (val + i + mix_factor) % 256
        encrypted.append(transformed_val)
        
    return encrypted

def coordinate_decrypt(encrypted_12: list[int]) -> list[int]:
    """
    Coordinate-based & Index-Mixing Backward Transformation (Decryption)
    - Forward transformation ကို Reverse (ပြန်လှန်) ၍ မူလ Array ကို ပြန်လည်ထုတ်ယူခြင်း။
    """
    decrypted = []
    for i, val in enumerate(encrypted_12):
        mix_factor = 0 if i == 0 else (i * 3) % 256
        
        # Reverse formula: (encrypted_val - index - mix_factor) % 256
        # Python တွင် negative values များအတွက် modulo မှန်ကန်စေရန် % 256 ကို သုံးပေးရပါမည်။
        original_val = (val - i - mix_factor) % 256
        decrypted.append(original_val)
        
    return decrypted

if __name__ == "__main__":
    print("=" * 65)
    print("   COORDINATE-BASED LOCAL TRANSFORMATION TEST")
    print("=" * 65)

    # 1. 12-element ပါဝင်သော Test Array တစ်ခု (Low-level chunk ဥပမာ)
    test_array = [77, 121, 32, 110, 97, 109, 101, 32, 75, 111, 32, 75]
    
    print(f"\n[INPUT] Original 12-Element Array:")
    print(f"  {test_array}")
    print(f"  Array Size: {len(test_array)} dimensions")

    # 2. Forward Transformation (Encryption - Coordinate Mapping & Mixing)
    print("\n[+] Applying Coordinate Forward Transformation...")
    encrypted_array = coordinate_encrypt(test_array)
    print(f"  Encrypted Array: {encrypted_array}")

    # 3. Backward Transformation (Decryption - Reverse Process)
    print("\n[+] Applying Coordinate Reverse Transformation...")
    restored_array = coordinate_decrypt(encrypted_array)
    print(f"  Restored Array : {restored_array}")

    print("\n" + "=" * 65)
    # 4. Integrity Verification (စစ်ဆေးခြင်း)
    if test_array == restored_array:
        print(">>> SUCCESS: Coordinate math logic verified 100% perfectly! <<<")
    else:
        print(">>> ERROR: Data mismatch in coordinate transformation! <<<")
    print("=" * 65)