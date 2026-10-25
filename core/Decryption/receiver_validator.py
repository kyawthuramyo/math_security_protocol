# =====================================================================
# [EN] Receiver Validator Layer: Pre-checks incoming packet stream count 
#      and metadata integrity before decryption processing.
# [MY] Receiver Validator အလွှာ- ရောက်ရှိလာသော Packet အရေအတွက်နှင့် 
#      Metadata မှန်ကန်မှုကို Decryption မလုပ်မီ ကြိုတင်စစ်ဆေးခြင်း။
# =====================================================================

class ReceiverValidator:
    def __init__(self, expected_cycle_limit: int = 1000):
        """
        [EN] Initialize with expected cycle limit (e.g., 1000 packets).
        [MY] မျှော်မှန်းထားသော cycle limit (ဥပမာ- Packet ၁၀၀၀) ဖြင့် စတင်ခြင်း။
        """
        self.expected_cycle_limit = expected_cycle_limit

    def validate_incoming_stream(self, mixed_stream: list, metadata: list) -> bool:
        """
        [EN] Validates that incoming packet stream and metadata counts match 
             the strict expected cycle limit. Raises error if tampered.
        [MY] ဝင်လာသော Packet အရေအတွက်နှင့် Metadata အရေအတွက်သည် သတ်မှတ်ထားသော 
             cycle limit နှင့် ကိုက်ညီမှုရှိမရှိ စစ်ဆေးသည်။ မကိုက်ညီပါက Error တက်မည်။
        """
        stream_len = len(mixed_stream)
        meta_len = len(metadata)

        if stream_len != self.expected_cycle_limit:
            raise ValueError(
                f"[RECEIVER SECURITY ALERT] Packet Count Mismatch! Expected: {self.expected_cycle_limit}, Got: {stream_len}. Potential Tampering Detected!"
            )

        if meta_len != self.expected_cycle_limit:
            raise ValueError(
                f"[RECEIVER SECURITY ALERT] Metadata Count Mismatch! Expected: {self.expected_cycle_limit}, Got: {meta_len}."
            )

        return True