# =====================================================================
# [EN] Decoy Filter Layer: Filters out decoy/fake chunks by checking 
#      if the packet index is a prime number within the 1-1000 cycle.
# [MY] Decoy Filter အလွှာ- ၁ မှ ၁၀၀၀ စက်ဝန်းအတွင်း Packet Index သည် Prime Number 
#      ဟုတ်မဟုတ် စစ်ဆေးခြင်းဖြင့် အတု (Decoy Chunks) များကို ဖယ်ထုတ်ပြီး 
#      အစစ်များကိုသာ စစ်ထုတ်ယူခြင်း။
# =====================================================================

class DecoyFilter:
    def __init__(self):
        """
        [EN] Initialize the Decoy Filter.
        [MY] Decoy Filter ကို စတင်ရန်။
        """
        pass

    def _is_prime(self, n: int) -> bool:
        """
        [EN] Helper method to check if a number is prime.
        [MY] နံပါတ်တစ်ခုသည် Prime ဟုတ်မဟုတ် စစ်ဆေးသည့် helper method။
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def filter_real_chunks(self, mixed_stream: list[list[int]], packet_metadata: list[dict]) -> list[list[int]]:
        """
        [EN] Filters the mixed stream using metadata indices, retaining only 
             chunks located at prime indices (Real Chunks).
        [MY] Metadata index များကို အသုံးပြု၍ Prime index များတွင် ရှိသော 
             (အစစ်ဖြစ်သော) Chunk များကိုသာ စစ်ထုတ်ယူသည်။
        """
        real_chunks = []

        for chunk, meta in zip(mixed_stream, packet_metadata):
            index = meta["index"]
            # [EN] Check if the index is prime; if so, it's a real chunk
            # [MY] Index သည် prime ဟုတ်ပါက အစစ်အဖြစ် သတ်မှတ်ယူသည်
            if self._is_prime(index):
                real_chunks.append(chunk)

        return real_chunks