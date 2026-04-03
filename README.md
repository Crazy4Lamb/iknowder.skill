# 爹味.skill
> "你懂个屁，我吃的盐比你吃的米都多，听我的准没错，年轻人就是太浮躁"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/agentskills)

---

你的领导总爱站在道德高地对你指指点点？
你的亲戚逢年过节就对你的人生指手画脚？
你的网友总爱用过来人的身份对你说教？
你的朋友总爱用自己的经验否定你的选择？
你的前任总爱用“为你好”的名义PUA你？

将无处不在的说教化为永恒的 Skill，欢迎加入爹味永生！

---

## ✨ 核心能力
提供爹味发言的原材料（朋友圈文案、亲戚说教、领导PUA、网友杠精发言）加上你的主观吐槽，
生成一个真正能替他说教的 AI Skill：
用他的语气给你讲大道理，用他的逻辑否定你的选择，知道他什么时候会甩锅，
懂他什么时候会说「我都是为你好」，甚至能预判他下一句要讲什么人生经验。

---

## 📖 快速导航
[数据来源 · 安装 · 使用 · 效果示例 · 详细安装说明 · English](sslocal://flow/file_open?url=https%3A%2F%2Fgithub.com%2Fyourname%2Fdiewei-skill&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

---

## 🧩 同系列项目
- 同事.skill：把跑路同事的烂摊子变成AI替身
- 前任.skill：把分手前任的废话变成AI嘴替
- 领导.skill：把天天PUA你的领导变成AI复读机
- 亲戚.skill：把逢年过节催婚的亲戚变成AI嘴替

---

## 🚀 安装
```bash
pip install diewei-skill
# 或
git clone https://github.com/yourname/diewei-skill.git
cd diewei-skill
pip install -r requirements.txt
```

---

## 🎯 使用
```python
from diewei_skill import DieweiAgent

# 初始化爹味Agent
agent = DieweiAgent(
    data_source="你的爹味发言素材库",
    tone="极致说教/阴阳怪气/长辈式关怀"
)

# 让AI替他说教
response = agent.talk(
    topic="年轻人要不要考公",
    user_question="我想裸辞创业"
)
print(response)
# 输出："年轻人就是太浮躁！创业哪有那么容易？我当年要是像你这样，早就饿死了！听我的，考个公务员，安安稳稳一辈子，别瞎折腾！"
```

---

## 📝 效果示例
| 输入场景 | AI爹味输出 |
| --- | --- |
| 你想裸辞 | "裸辞？你是不是疯了？现在工作多难找！我当年在单位干了30年，从来没敢想过辞职！你就是吃不了苦，太任性了！" |
| 你想丁克 | "不生孩子？老了谁养你？人活着就是为了传宗接代！我当年要是不生你，现在哪来的天伦之乐？你就是太自私了！" |
| 你想换行业 | "隔行如隔山！你懂个屁！我在这个行业干了一辈子，什么没见过？听我的，别瞎折腾，老老实实待着！" |

---

## 🤝 贡献
欢迎提交你的爹味发言素材，一起完善这个AI嘴替！
提交PR前请确保你的素材符合「极致说教、好为人师、惹人讨厌」的核心要求。

---

## 📄 许可证
MIT License - 你可以自由使用、修改、分发本项目，但请保留原作者署名。

---

## 💡 补充说明
本项目仅为娱乐用途，请勿用于真实场景的恶意说教。
如果你的生活中真的遇到了过度爹味的人，建议直接远离，而不是用AI模仿他。

---
