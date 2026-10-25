import random

class DecoyInjector:
    def __init__(self, cycle_limit: int = 1000):
        """
        Initialize the Decoy Injector with a cycle limit (e.g., 1000).
        Prime indices တွင် အစစ်များ၊ Non-prime တွင် အတုများ ထည့်သွင်းရန်။
        """
        self.cycle_limit = cycle_limit

    def _is_prime(self, n: int) -> bool:
        """
        Check if a number is prime.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def inject_decoys(self, real_chunks: list[list[int]]) -> tuple[list[list[int]], list[dict]]:
        """
        Inject decoy/fake chunks into non-prime indices within the cycle limit,
        placing real chunks sequentially into prime indices.
        """
        mixed_stream = []
        packet_metadata = [] # To help receiver identify real vs decoy
        
        real_idx = 0
        total_real = len(real_chunks)

        for current_index in range(1, self.cycle_limit + 1):
            if self._is_prime(current_index):
                if real_idx < total_real:
                    # Place Real Chunk at Prime Index
                    mixed_stream.append(real_chunks[real_idx])
                    packet_metadata.append({"index": current_index, "is_real": True})
                    real_idx += 1
                else:
                    # If we run out of real chunks, fill with decoy or pad
                    dummy_chunk = [random.randint(0, 255) for _ in range(len(real_chunks[0]))]
                    mixed_stream.append(dummy_chunk)
                    packet_metadata.append({"index": current_index, "is_real": False})
            else:
                # Place Decoy/Fake Chunk at Non-Prime Index
                if real_chunks:
                    dummy_chunk = [random.randint(0, 255) for _ in range(len(real_chunks[0]))]
                else:
                    dummy_chunk = [random.randint(0, 255) for _ in range(12)]
                
                mixed_stream.append(dummy_chunk)
                packet_metadata.append({"index": current_index, "is_real": False})

        return mixed_stream, packet_metadata