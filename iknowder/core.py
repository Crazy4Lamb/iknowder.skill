import random

class IknoWder:
    def __init__(self, mode="buddha"):
        self.mode = mode
        # 摆烂语录池，无厘头+有梗
        self.lines = [
            "我知道个 der，别问我。",
            "不懂，不评价，不参与。",
            "别问我，我啥也不知道，啥也不想知道。",
            "你说得都对，而我知道个 der。",
            "建议？我自己都活不明白，别害我。",
            "大脑已关机，只知道个 der。",
            "别问为什么，问就是我知道个 der。",
            "我只是个路过的，啥也不懂。",
            "不负责、不判断、不纠结，我知道个 der。",
            "别为难我了，我真知道个 der。"
        ]

    def say(self, input_text: str = "") -> str:
        text = input_text.strip().lower()

        # 高频关键词触发精准摆烂
        if any(k in text for k in ["怎么看", "怎么想", "看法"]):
            return random.choice([
                "不看不想不评价，我知道个 der。",
                "没看法，别问我，问就是 der。"
            ])

        elif any(k in text for k in ["建议", "怎么办", "该怎么做"]):
            return random.choice([
                "别找我要建议，我自己都一团糟。",
                "建议个 der，爱咋咋地。"
            ])

        elif any(k in text for k in ["懂吗", "明白吗", "知道吗"]):
            return random.choice([
                "懂？我懂个 der。",
                "不明白，也不想明白。"
            ])

        elif any(k in text for k in ["为什么", "咋回事", "原因"]):
            return random.choice([
                "别问为什么，问就是我知道个 der。",
                "原因个 der，摆烂就完事了。"
            ])

        elif any(k in text for k in ["靠谱吗", "行不行", "厉害吗"]):
            return random.choice([
                "我靠谱个 der。",
                "不行，别问，问就是不行。"
            ])

        # 通用摆烂，随机一句
        return random.choice(self.lines)