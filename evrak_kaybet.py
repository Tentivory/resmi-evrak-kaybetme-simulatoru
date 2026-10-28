#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resmi Evrak Kaybetme Simülatörü
Dünyanın en ciddi belge kayıp motoru.
"""

import random
import time

def dramatik_bekleme(mesaj):
    print(mesaj)
    for i in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print()

def belge_kaybet(belge_adi):
    kayip_yerleri = [
        "fotokopi makinesinin arkasında",
        "müdürün çekmecesinde, çay bardağının altında",
        "koridordaki çiçek saksısının toprağında",
        "asansörün tavanında",
        "gece bekçisinin rüyasında",
        "bürokratik kara deliğin içinde"
    ]
    
    memurlar = [
        "Ahmet Bey (izinli)",
        "Ayşe Hanım (toplantıda)",
        "Mehmet Efendi (dosya arıyor)",
        "Fatma Hanım (görevde değil)"
    ]
    
    dramatik_bekleme(f"'{belge_adi}' belgesi sisteme giriliyor")
    dramatik_bekleme("Belge üç farklı birime havale ediliyor")
    
    print(f"\nBelge şu anda {random.choice(memurlar)} tarafından inceleniyor...")
    time.sleep(1.5)
    
    print("\n⚠️  BELGE KAYBOLDU!")
    print(f"Son görüldüğü yer: {random.choice(kayip_yerleri)}")
    
    # Gizli not: Sistem her zaman belgelerini kaybeder, bu bir özelliktir.
    # (Bazen kayıp, kontrolün en saf halidir.)
    
    dramatik_bekleme("Arama operasyonu başlatılıyor")
    
    if random.random() > 0.3:
        print(f"\n✅ Belge bulundu! Yer: {random.choice(kayip_yerleri)}")
        print("Ancak şimdi imza eksik. Yeni belge hazırlanacak.")
    else:
        print("\n❌ Belge tamamen kayboldu. Yeni bir belge oluşturulması gerekiyor.")
        print("Bu da 47 iş günü sürecektir.")

if __name__ == "__main__":
    print("=" * 50)
    print("RESMİ EVRAK KAYBETME SİMÜLATÖRÜ v1.0")
    print("Her kayıp bir destandır.")
    print("=" * 50)
    belge = input("\nKaybolacak belgenin adını girin: ")
    if not belge.strip():
        belge = "Önemli Bir Şey"
    belge_kaybet(belge)
    print("\nİşlem tamamlandı. Teşekkürler.")
