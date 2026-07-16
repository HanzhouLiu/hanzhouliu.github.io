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

Howdy! I am a 5th-year Ph.D. student in Computer Engineering at Texas A&M University. 

My research began with image restoration. Then, my focus took a foray into feed-forward 3D vision. Meanwhile, I also have hands-on experience on supervised fine-tuning and reinforcement learning.

I am actively seeking full-time opportunities for 2027. If you are aware of relevant openings, please feel free to contact me at heyhanzhou@gmail.com.

<!--My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).
-->

# 🔥 News
- *2026.05*: &nbsp;🎉🎉 I am joining [Amazon Store](https://www.aboutamazon.com/what-we-do/amazon-store) as an applied scientist intern, supervised by [Rui Song](https://song-ray.github.io/), working on LLM post-training. Let us have a coffee chat in Seattle!
- *2026.01*: &nbsp;🎉🎉 Our paper [Stylos](https://hanzhouliu.github.io/Stylos/) on feed-forward 3d stylization is now accepted by ICLR 2026 (Review Scores 8-8-6-6, <strong>Top 1.3%</strong>).
- *2025.08*: &nbsp;🎉🎉 I am joining the Urban Resilience Lab as a research assitant, supervised by [Ali Mostafavi](https://scholar.google.com/citations?user=DFNvQPYAAAAJ&hl=en), working on cross-table geospatial reasoning. 
- *2025.04*: &nbsp;🎉🎉 [XYScanNet](https://openaccess.thecvf.com/content/CVPR2025W/NTIRE/papers/Liu_XYScanNet_A_State_Space_Model_for_Single_Image_Deblurring_CVPRW_2025_paper.pdf) has been accepted by NTIRE CVPR 2025. See you in Nashville!
- *2024.02*: &nbsp;🎉🎉 [Mamba4rec](https://github.com/chengkai-liu/Mamba4Rec) has been selected as the Best Paper Award for KDD'24 Resource-efficient Learning for Knowledge Discovery Workshop (RelKD’24). 

# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026 (8-8-6-6)</div><img src='images/stylos.png' alt="stylos" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Stylos: Multi-View 3D Stylization with Single-Forward Gaussian Splatting](https://arxiv.org/pdf/2509.26455)  
**Hanzhou Liu\***, Jia Huang, Mi Lu, Srikanth Saripalli, **Peng Jiang\*** †, *ICLR 2026*  

[**Project**](https://github.com/HanzhouLiu/Stylos) ｜ [**Demo**](https://huggingface.co/spaces/HanzhouLiu/Stylos_Gradio) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:Wp0gIr-vW9MC'></span></strong>  
- Stylos couples **VGGT** with **Gaussian Splatting** for cross-view style transfer, introducing a voxel-based style loss to ensure **multi-view consistency**.  

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NTIRE CVPR 2025</div><img src='images/xyscannet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[XYScanNet: A State Space Model for Single Image Deblurring](https://arxiv.org/pdf/2412.10338)  
**Hanzhou Liu**, Chengkai Liu, Jiacong Xu, Peng Jiang, Mi Lu, **NTIRE CVPR 2025**

[**Project**](https://github.com/HanzhouLiu/XYScanNet) ｜ [**Demo**](https://huggingface.co/spaces/HanzhouLiu/XYScanNet_Demo)
<strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- XYScanNet, maintains competitive distortion metrics and significantly improves perceptual performance. Experimental results show that XYScanNet enhances KID by 17% compared to the nearest competitor. 
</div>
</div>

- [Mamba4rec: Towards efficient sequential recommendation with selective state space models](https://github.com/chengkai-liu/Mamba4Rec)  
Chengkai Liu, Jianghao Lin, Jianling Wang, Hanzhou Liu, James Caverlee, **RelKD KDD 2024 Best Paper Award**

- [Behavior-Dependent Linear Recurrent Units for Efficient Sequential Recommendation](https://github.com/chengkai-liu/RecBLR)  
Chengkai Liu, Jianghao Lin, Hanzhou Liu, Jianling Wang, James Caverlee, **CIKM 2024**

- [Real-world image deblurring via unsupervised domain adaptation](https://link.springer.com/chapter/10.1007/978-3-031-47966-3_12)  
Hanzhou Liu, Binghan Li, Mi Lu, Yucheng Wu, **ISVC 2023**

<!--# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

# 📖 Educations
- *2021.08 - now*, Texas A&M University, PhD in Computer Engineering. 
- *2019.08 - 2021.06*, Texas A&M University, MS in Computer Engineering. 
- *2014.08 - 2018.06*, Jilin University, BS in Electrical Engineering. 

# 💬 Invited Talks
- *2024.07*, **Mamba4Rec**, invited talk at Uber.

# 🧾 Community Services
- *2026*, Reviewer, NeurIPS 2026.
- *2026*, Reviewer, Transactions on Consumer Electronics (TCE).
- *2025*, Reviewer, New Trends in Image Restoration and Enhancement workshopin conjunction with CVPR 2025 (NTIRE).
- *2024*, Reviewer,  IEEE/CVF Winter Conference on Applications of Computer Vision (WACV).
- *2024*, Reviewer, The Conference on Information and Knowledge Management (CIKM).

<!--# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.-->