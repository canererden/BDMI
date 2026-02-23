# Contributing

Katkılar memnuniyetle karşılanır.

## Katkı Kuralları

1. Her değişiklik için kısa ve açıklayıcı bir branch adı kullanın.
2. Notebook güncellemelerinde:
   - Çıktıları temizleyin (mümkünse)
   - Hücre sırasını bozmayın
   - Gereksiz büyük binary çıktı üretmeyin
3. Yeni notebook eklerken dosya adını bölüm numarasıyla başlatın.
4. Pull Request açıklamasında:
   - Ne değişti?
   - Neden değişti?
   - Etkilenen notebook(lar)
5. Kod/örnekler için telif ve kaynak gösterimine dikkat edin.

## Yerel Doğrulama

```bash
python scripts/validate_notebooks.py
```

## Commit Mesajı Önerisi

- feat: yeni notebook / yeni bölüm örneği
- fix: hata düzeltmesi
- docs: açıklama veya README iyileştirmesi
- chore: bakım, yapılandırma, workflow
