class GlobalReverseTransformer:
    def __init__(self, batch_size: int = 100):
        """
        Initialize the Global Reverse Transformer with a batch size.
        သတ်မှတ်ထားသော batch_size ဖြင့် GlobalReverseTransformer ကို စတင်ခြင်း။
        """
        self.batch_size = batch_size

    def reverse_global(self, shuffled_chunks: list[list[int]], shuffle_metadata: list[int]) -> list[list[int]]:
        """
        Search and sort shuffled chunks back to their original order using prime metadata.
        Prime Metadata များကို အသုံးပြု၍ ရှာဖွေကာ (Search & Sort) Chunk များကို မူလအစီအစဉ်အတိုင်း ပြန်စီခြင်း။
        """
        restored_chunks = []
        chunk_idx = 0

        # Process batch by batch / Batch တစ်ခုချင်းစီအလိုက် ပြန်လည်ဖော်ထုတ်ခြင်း
        for i in range(0, len(shuffled_chunks), self.batch_size):
            # Get the current batch of chunks and their weights
            current_batch_chunks = shuffled_chunks[i:i + self.batch_size]
            current_weights = shuffle_metadata[i:i + self.batch_size]
            batch_len = len(current_batch_chunks)

            # Combine chunks back with their weights
            paired = list(zip(current_weights, current_batch_chunks))

            # Search and Sort: Sort back by prime weight to restore original sequential order
            # Search & Sort ပြုလုပ်ခြင်း - Prime weight များကို အခြေခံ၍ မူလအစဉ်အတိုင်း ပြန်လည်စီစစ်ခြင်း
            paired.sort(key=lambda x: x[0])

            # Extract original ordered chunks
            original_batch = [item[1] for item in paired]
            restored_chunks.extend(original_batch)

        return restored_chunks