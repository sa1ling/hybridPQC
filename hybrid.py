import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import rc

# 1️⃣ 한글 폰트 설정 (Windows용)
rc('font', family='Malgun Gothic')

# 2️⃣ 그래프 생성
G = nx.DiGraph()

# PQC 구조 노드 추가
G.add_edges_from([
    ("메시지 m", "해시 H(m)"),
    ("해시 H(m)", "격자 서명 s1\n(LWE/NTRU 기반)"),
    ("격자 서명 s1\n(LWE/NTRU 기반)", "해시 기반 인증 s2\n(Merkle/WOTS+)"),
    ("해시 기반 인증 s2\n(Merkle/WOTS+)", "최종 서명 (s1,s2)")
])

# 3️⃣ 노드 위치 (간단한 top-down 느낌)
pos = nx.spring_layout(G, seed=42)  # seed 고정으로 항상 같은 위치

# 4️⃣ 그림 그리기
plt.figure(figsize=(10,6))
nx.draw(G, pos,
        with_labels=True,
        node_size=4500,
        node_color="#FFFFFF",   # 흰색 배경
        font_size=10,
        font_weight='bold',
        font_family='Malgun Gothic',  # 한글 적용
        edgecolors="#000000",
        linewidths=1.5,
        arrows=True,
        arrowstyle='-|>',
        arrowsize=15)

plt.title("격자+해시 하이브리드 양자 내성 서명 구조", fontsize=14, fontweight="bold")
plt.axis("off")

# 5️⃣ 논문용 PNG 저장 (고해상도)
plt.savefig("hybrid_pqc_structure.png", dpi=600, bbox_inches="tight", transparent=False)
plt.show()
