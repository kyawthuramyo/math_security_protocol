import random

class GlobalForwardTransformer:
    def __init__(self, batch_size: int = 100):
        """
        Initialize the Global Forward Transformer with a batch size.
        သတ်မှတ်ထားသော batch_size (ဥပမာ - ၁၀၀) ဖြင့် GlobalForwardTransformer ကို စတင်ခြင်း။
        """
        self.batch_size = batch_size

    def _generate_primes(self, n: int) -> list[int]:
        """
        Generate first n prime numbers.
        ပထမဆုံး Prime Numbers n လုံးကို ရှာဖွေထုတ်လုပ်ပေးခြင်း။
        """
        primes = []
        num = 2
        while len(primes) < n:
            is_prime = True
            for p in primes:
                if p * p > num:
                    break
                if num % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
            num += 1
        return primes

    def transform_global(self, chunks: list[list[int]]) -> tuple[list[list[int]], list[int]]:
        """
        Group chunks into batches, map with reverse prime indices, and shuffle.
        Chunk များကို အစုလိုက်ခွဲ၍ Prime numbers များဖြင့် Index ချိတ်ကာ နေရာရောနှောခြင်း (Global Shuffling)။
        """
        shuffled_chunks = []
        shuffle_metadata = [] # To store sorting keys for decryption / Decryption အတွက် ပြန်စီမည့် အချက်အလက်များ သိမ်းရန်

        # Process in batches (e.g., 100 chunks per batch) / Batch တစ်ခုချင်းစီ (ဥပမာ - ၁၀၀ စီ) ခွဲ၍ လုပ်ဆောင်ခြင်း
        for i in range(0, len(chunks), self.batch_size):
            batch = chunks[i:i + self.batch_size]
            current_batch_size = len(batch)

            # Generate first N primes for this batch / ဤ batch အတွက် Prime numbers များကို ထုတ်ခြင်း
            primes = self._generate_primes(current_batch_size)

            # Create reverse prime mapping (100th prime maps to index 0, etc.)
            # Prime numbers များကို ပြန်လှန်၍ Index များနှင့် ချိတ်ဆက်ခြင်း (Reverse Prime Mapping)
            indexed_batch = []
            for idx, chunk in enumerate(batch):
                # Use reverse prime order as the sorting/mapping weight
                prime_weight = primes[current_batch_size - 1 - idx]
                indexed_batch.append((prime_weight, chunk))

            # Shuffle deterministically or randomly based on prime weights
            # Prime weights ကို အခြေခံ၍ နေရာရောနှောခြင်း
            # Note: For robust tracking, we keep the prime weight attached to the chunk
            combined = list(indexed_batch)
            
            # Sort or shuffle using a fixed deterministic seed or random based on weights
            # ဒီနေရာတွင် Prime weight များကို အခြေခံ၍ Shuffling ပြုလုပ်ပါမည်
            random.seed(42) # Fixed seed for protocol consistency (သို့မဟုတ် dynamic seed သုံးနိုင်ပါသည်)
            
            # Create a copy to shuffle while keeping track of original weights
            indexed_mapping = []
            for p_weight, chunk in combined:
                indexed_mapping.append((p_weight, chunk))
            
            # Shuffle the batch chunks
            random.shuffle(indexed_mapping)

            # Extract shuffled chunks and their corresponding prime weights (metadata)
            final_batch_chunks = [item[1] for item in indexed_mapping]
            batch_weights = [item[0] for item in indexed_mapping]

            shuffled_chunks.extend(final_batch_chunks)
            shuffle_metadata.extend(batch_weights)

        return shuffled_chunks, shuffle_metadata