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
        shuffled_chunks = []
        shuffle_metadata = []

        for i in range(0, len(chunks), self.batch_size):
            batch = chunks[i:i + self.batch_size]
            current_batch_size = len(batch)

            primes = self._generate_primes(current_batch_size)

            indexed_batch = []
            for idx, chunk in enumerate(batch):
                prime_weight = primes[current_batch_size - 1 - idx]
                indexed_batch.append((prime_weight, chunk))

            # --- [ပြင်ဆင်ရန်] ---
            # Prime weight များကို အခြေခံ၍ တကယ့် Diffusion (Random/Permutation) ဖြစ်စေရန် 
            # ဥပမာ - prime weight များကို key အဖြစ်သုံးပြီး random shuffle လုပ်ခြင်း (သို့မဟုတ်) 
            # prime များကို index အဖြစ် တွက်ချက်၍ နေရာလွဲပေးခြင်း
            import random
            # Deterministic ဖြစ်စေရန် prime weights ပေါင်းုစုမှုကို seed အဖြစ် သုံးနိုင်သည်
            seed_val = sum(primes)
            rng = random.Random(seed_val)
            
            # Batch ထဲရှိ chunk များကို အမှန်တကယ် နေရာလွဲပေးခြင်း (Permutation)
            rng.shuffle(indexed_batch)
            # -------------------

            final_batch_chunks = [item[1] for item in indexed_batch]
            batch_weights = [item[0] for item in indexed_batch]

            shuffled_chunks.extend(final_batch_chunks)
            shuffle_metadata.extend(batch_weights)

        return shuffled_chunks, shuffle_metadata