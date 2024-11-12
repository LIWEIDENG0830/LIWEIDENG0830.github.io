---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm a fourth year PhD candidate at [School of Computer Science and Engineering](https://www.scse.uestc.edu.cn/), [University of Electronic Science and Technology of China](https://www.uestc.edu.cn/), supervised by Prof. [Kai Zheng](https://zheng-kai.com/). Moreover, I am co-supervised by Dr. [Yan Zhao](https://yan20191113.github.io), an Associate Professor at Aalborg University. Previously, I received my M.E. and B.E. degree from University of Electronic Science and Technology of China and Taiyuan University of Technology in 2018 and 2021, respectively. 

My research interests include spatio-temporal data mining, trajectory computing, finance technology, recommender system, vector database, and other data-driven applications. 

<!-- 
My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). 
<a href='https://scholar.google.com/citations?user=IjStiDYAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fliweideng0830%2Fliweideng0830.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
-->


# 🔥 News
- *2024.10*: &nbsp;🎉🎉 One paper is accepted by VLDB 2025. 
- *2024.05*: &nbsp;🎉🎉 One paper is accepted by KDD 2024. 
- *2023.11*: &nbsp;🎉🎉 Three papers are accepted by ICDE 2024.

# 📝 Publications 

<!-- 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>

- [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020**
-->

**Selected Journal Papers**
1. **\[VLDBJ\]** Yan Zhao, Kai Zheng, Ziwei Wang, **Liwei Deng**, Bin Yang, Torben Bach Pedersen, Christian S Jensen, Xiaofang Zhou. Coalition-based task assignment with priority-aware fairness in spatial crowdsourcing. In VLDBJ.
2. **\[TOIS\]** Yan Zhao<sup>+</sup>, **Liwei Deng<sup>+</sup>**, Kai Zheng. AdaTaskRec: An adaptive task recommendation framework in spatial crowdsourcing. In TOIS.
3. **\[TIST\]** **Liwei Deng**, Hao Sun, Rui Sun, Yan Zhao, Han Su. Efficient and effective similar subtrajectory search: a spatial-aware comprehension approach. In TIST.
4. **\[WWWJ\]** Xuanhao Chen, **Liwei Deng**, Yan Zhao, Xiaofang Zhou, Kai Zheng. Community-based influence maximization in location-based social network. In WWWJ.

**Selected Conference Papers**

1. **\[Arxiv\]** Tianfu Wang, Long Yang, Chao Wang, Chuan Qin, **Liwei Deng**, Li Shen, Hui Xiong. Towards Constraint-aware Learning for Resource Allocation in NFV-enabled Networks. Arxiv Preprint 2025.
2. **\[VLDB\]** **Liwei Deng**, Tianfu Wang, Yan Zhao, Kai Zheng. MILLION: A General Multi-Objective Framework with Controllable Risk for Portfolio Management. In PVLDB 2025.
3. **\[KDD\]** Tianfu Wang, **Liwei Deng**, Chao Wang, Jianxun Lian, Yue Yan, Nicholas Jing Yuan, Qi Zhang, Hui Xiong. COMET: NFT Price Prediction with Wallet Profiling. In KDD 2025.
4. **\[ICDE\]** **Liwei Deng**, Yan Zhao, Yue Cui, Yuyang Xia, Jin Chen, Kai Zheng. Task Recommendation in Spatial Crowdsourcing: A Trade-Off Between Diversity and Coverage. In ICDE 2024.
5. **\[ICDE\]** **Liwei Deng**, Yan Zhao, Jin Chen, Shuncheng Liu, Yuyang Xia, Kai Zheng. Learning to Hash for Trajectory Similarity Computation and Search. In ICDE 2024.
6. **\[ICDE\]** Yuyang Xia, Shuncheng Liu, Quanlin Yu, **Liwei Deng**, You Zhang, Han Su, Kai Zheng. Parameterized Decision-Making with Multi-Modality Perception for Autonomous Driving. In ICDE 2024.
7. **\[ACL\]** Hao Sun, Yang Li, **Liwei Deng**, Bowen Li, Binyuan Hui, Binhua Li, Yunshi Lan, Yan Zhang, Yongbin Li. History semantic graph enhanced conversational KBQA with temporal information modeling. In ACL 2023.
8. **\[DASFAA\]** **Liwei Deng**, Yan Zhao, Hao Sun, Changjie Yang, Jiandong Xie, Kai Zheng. Fusing Local and Global Mobility Patterns for Trajectory Recovery. In DASFAA 2023.
9. **\[DASFAA\]** Yupu Zhang, **Liwei Deng**, Yan Zhao, Jin Chen, Jiandong Xie, Kai Zheng. SimiDTR: Deep Trajectory Recovery with Enhanced Trajectory Similarity. In DASFAA 2023. **(Best Student Paper Award Runner Up)**
10. **\[WSDM\]** **Liwei Deng**, Hao Sun, Yan Zhao, Shuncheng Liu, Kai Zheng. S2tul: A semi-supervised framework for trajectory-user linking. In WSDM 2023.
11. **\[WSDM\]** Xuanhao Chen, **Liwei Deng**, Yan Zhao, Kai Zheng. Adversarial autoencoder for unsupervised time series anomaly detection and interpretation. In WSDM 2023.
12. **\[CIKM\]** Jiaxin Liu, **Liwei Deng**, Hao Miao, Yan Zhao, Kai Zheng. Task assignment with federated preference learning in spatial crowdsourcing. In CIKM 2022.
13. **\[CIKM\]** **Liwei Deng**, Yan Zhao, Zidan Fu, Hao Sun, Shuncheng Liu, Kai Zheng. Efficient trajectory similarity computation with contrastive learning. In CIKM 2022.
14. **\[CIKM\]** Shuncheng Liu, Xu Chen, Ziniu Wu, **Liwei Deng**, Han Su, Kai Zheng. HeGA: heterogeneous graph aggregation network for trajectory prediction in high-density traffic. In CIKM 2022.
15. **\[KDD\]** Jin Chen, Guanyu Ye, Yan Zhao, Shuncheng Liu, **Liwei Deng**, Xu Chen, Rui Zhou, Kai Zheng. Efficient join order selection learning with graph-based representation. In KDD 2022.
16. **\[MDM\]** Dazhuo Qiu, Yihao Wang, Yan Zhao, **Liwei Deng**, Kai Zheng. CityCross: Transferring Attention-based Knowledge for Location-based Advertising Recommendation. In MDM 2022. **(Best Industry, Systems and Apps Award)**
17. **\[WWW\]** Yan Zhao, Xuanhao Chen, **Liwei Deng**, Tung Kieu, Chenjuan Guo, Bin Yang, Kai Zheng, Christian S Jensen. Outlier detection for streaming task assignment in crowdsourcing. In WWW 2022.
18. **\[ICBK\]** Bingke Xu, Yue Cui, Zipeng Sun, **Liwei Deng**, Kai Zheng. Fair representation learning in knowledge-aware recommendation. In ICBK 2021.
19. **\[CCIS\]** Yan Zhao, Lianming Zhou, **Liwei Deng**, Vincent W Zheng, Hongzhi Yin, Kai Zheng. Subgraph convolutional network for recommendation. In CCIS 2021.
20. **\[CIKM\]** Hao Sun<sup>+</sup>, Changjie Yang<sup>+</sup>, **Liwei Deng<sup>+</sup>**, Fan Zhou, Feiteng Huang, Kai Zheng. Periodicmove: Shift-aware human mobility recovery with graph neural network. In CIKM 2021.
21. **\[VLDB\]** Yue Cui, Kai Zheng, Dingshan Cui, Jiandong Xie, **Liwei Deng**, Feiteng Huang, Xiaofang Zhou. METRO: a generic graph neural network framework for multivariate time series forecasting. In VLDB 2021.
22. **\[ICDE\]** Xuanhao Chen, **Liwei Deng**, Feiteng Huang, Chengwei Zhang, Zongquan Zhang, Yan Zhao, Kai Zheng. Daemon: Unsupervised anomaly detection and interpretation for multivariate time series. In ICDE 2021.
23. **\[DASFAA\]** Hao Sun, Zijian Wu, Yue Cui, **Liwei Deng**, Yan Zhao, Kai Zheng. Personalized dynamic knowledge-aware recommendation with hybrid explanations. In DASFAA 2021.
24. **\[KDD\]** Yue Cui, **Liwei Deng**, Yan Zhao, Bin Yao, Vincent W Zheng, Kai Zheng. Hidden poi ranking with spatial crowdsourcing. In KDD 2019.

**Note**: <sup>#</sup> and <sup>+</sup> indicate the corresponding author and co-first author

# 📖 Educations
- *2014.09 - 2018.06*, Taiyuan University of Technology, Bachelor
  - Information and Computing Science, School of Mathematics
- *2018.09 - 2021.06*, University of Electronic Science and Technology of China, Master
  - Computer Technology, School of Computer Science and Engineering
- *2021.09 - present*, University of Electronic Science and Technology of China, Ph.D.
  - Computer Science and Technology, School of Computer Science and Engineering

# 💻 Internships

- *2019.09 - 2020.07*, Huawei Cloud Database Innovation Lab, Huawei Technologies Co. Ltd., Chengdu, China.
  - Time Series Analysis
- *2023.08 - 2024.05*, Microsoft Internet Engineering Institute, Microsoft, Suzhou, China.
  - Finance Technology
  - Mentor: [Nicholas Jing Yuan](https://scholar.google.com/citations?user=B-d1EHAAAAAJ&hl=zh-CN)

# 🎖 Honors and Awards
- Best Student Paper Award Runner Up at DASFAA 2023
- Second-class People's Scholarship (2022, 2023, 2024)
- Best industry, systems and apps award at MDM 2022
- Second-class People's Scholarship (2020)
- First-class People's Scholarship (2019)
- First-class People's Scholarship (2015, 2016, 2017)

# ⏳ Professional Services

#### PC Member and Reviewer
- 2024: KDD, IJCAI, CIKM
- 2023: IJCAI, CIKM, AAAI

#### Journal Invited Reviewer
- TKDE, Information Processing and Management, IEEE Transactions on Cybernetics
