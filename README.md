# BDMI — Büyük Dil Modellerinin İnşası (Notebooks Repository)

Bu depo, **Büyük Dil Modellerinin İnşası** kitabının uygulama tarafını içeren Jupyter Notebook koleksiyonudur.

> Bu repoda kitap metni/bölüm içerikleri bulunmaz. Yalnızca notebook tabanlı uygulamalar, örnekler ve yardımcı dosyalar yer alır.

## Kapsam

- LLM temel kavramları
- Veri işleme, tokenizasyon ve embedding akışı
- Dikkat mekanizmaları (attention)
- Sıfırdan GPT uygulamaları
- Performans değerlendirmesi
- İnce ayar (fine-tuning)
- Komut mühendisliği
- LLM gelecek perspektifi

## Bölüm Notebooks

| Bölüm | Notebook |
|---|---|
| 03 — LLM'ler Nasıl Çalışır? | notebooks/03-nasil-calisir.ipynb |
| 04 — Dikkat | notebooks/04-dikkat.ipynb |
| 05 — Sıfırdan GPT | notebooks/05-sifirdan-gpt.ipynb |
| 06 — Performans Değerlendirmesi | notebooks/06-performans-degerlendirmesi.ipynb |
| 07 — İnce Ayar | notebooks/07-ince-ayar.ipynb |
| 08 — Komut Mühendisliği | notebooks/08-komut-muhendisligi.ipynb |
| 08 — Otonom Akademik Hakem Sistemi | notebooks/08-Otonom Akademik Hakem Sistemi/academic_review.ipynb |
| 09 — Gelecek | notebooks/09-gelecek.ipynb |

## Hızlı Başlangıç

### 1) Ortam Kurulumu

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Jupyter ile Çalıştırma

```bash
jupyter lab
```

## Dizin Yapısı

```text
BDMI/
├── notebooks/
├── scripts/
├── .github/workflows/
├── requirements.txt
├── environment.yml
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── README.md
```

## Referans


## Lisans

Bu depodaki kodlar MIT lisansı ile lisanslanmıştır. Ayrıntı için LICENSE dosyasına bakın.
