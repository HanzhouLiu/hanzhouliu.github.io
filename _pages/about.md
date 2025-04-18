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

Howdy! I’m a Ph.D. student at Texas A&M University, where I focus on algorithm design for Intelligent Transportation Systems (ITS) to tackle real-world challenges in low-level computer vision.

My research emphasizes on restoring high-quality images from degraded or blurred inputs. I leverage state-of-the-art techniques, including Generative Adversarial Networks (GANs), Transformers, and State Space Models (SSMs), to push the boundaries of image restoration.

In addition to 2D vision, I have hands-on experience with 3D scene segmentation using large-scale multi-modal datasets. My work involves training and deploying deep models on GPU clusters, with a strong focus on scalability and efficiency.

Lately, I’ve been exploring Vision-Language Models (VLMs) and sequence modeling, aiming to develop more holistic and interpretable solutions for both image and video understanding.

<!--My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).
-->

# 🔥 News
- *2025.04*: &nbsp;🎉🎉 [XYScanNet](https://arxiv.org/pdf/2412.10338) has been accepted by NTIRE CVPR 2025. See you in Nashville. 
- *2024.02*: &nbsp;🎉🎉 [Mamba4rec](https://github.com/chengkai-liu/Mamba4Rec) has been selected as the Best Paper Award for KDD'24 Resource-efficient Learning for Knowledge Discovery Workshop (RelKD’24). 

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NTIRE CVPR 2025</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[XYScanNet: A State Space Model for Single Image Deblurring](https://arxiv.org/pdf/2412.10338)
**Hanzhou Liu**, Chengkai Liu, Jiacong Xu, Peng Jiang, Mi Lu

[**Project**](https://github.com/HanzhouLiu/XYScanNet) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- XYScanNet, maintains competitive distortion metrics and significantly improves perceptual performance. Experimental results show that XYScanNet enhances KID by 17% compared to the nearest competitor. 
</div>
</div>

- [Mamba4rec: Towards efficient sequential recommendation with selective state space models](https://github.com/chengkai-liu/Mamba4Rec), Chengkai Liu, Jianghao Lin, Jianling Wang, Hanzhou Liu, James Caverlee, **RelKD KDD 2024 Best Paper Award**

- [Behavior-Dependent Linear Recurrent Units for Efficient Sequential Recommendation](https://github.com/chengkai-liu/RecBLR), Chengkai Liu, Jianghao Lin, Hanzhou Liu, Jianling Wang, James Caverlee, **CIKM 2024**

- [Real-world image deblurring via unsupervised domain adaptation](https://link.springer.com/chapter/10.1007/978-3-031-47966-3_12), Hanzhou Liu, Binghan Li, Mi Lu, Yucheng Wu, **ISVC 2023**

<!--# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

# 📖 Educations
- *2021.08 - now*, Texas A&M University, PhD in Computer Engineering. 
- *2019.08 - 2021.06*, Texas A&M University, MS in Computer Engineering. 
- *2014.08 - 2018.06*, Jilin University, BS in Electrical Engineering. 

# 💬 Invited Talks
- *2024.07*, **Mamba4Rec**, invited talk at Uber.

# 🧾 Academic Service
- *2025*, Reviewer, IEEE Transactions on Image Processing (TIP).
- *2024*, Reviewer, The Conference on Information and Knowledge Management (CIKM).
- *2024*, Reviewer, NTIRE: New Trends in Image Restoration and Enhancement workshopin conjunction with CVPR 2025.
<!--# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.-->