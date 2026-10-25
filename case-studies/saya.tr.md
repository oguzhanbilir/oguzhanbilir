Türkçe | [English](saya.md)

# SAYA Sağlıklı Yaşam

Çocuk ve ergen obezitesi giderek büyüyen bir sorun ve bu yaşta edinilen alışkanlıklar kalıcı oluyor.

## Nedir

10-17 yaş için sağlıklı beslenme ve hareket alışkanlığı kazandırmayı amaçlayan bir Android uygulaması. Benim danışmanlığımda iki ortaokul öğrencisi tasarlayıp kodladı.

## Öne çıkanlar

- Kayıttaki kısa anketle günlük görevler kişiselleşiyor
- Görevleri tamamlamaya ve devamlılığa göre puan, lig ve ödül
- Hedef kitleyle test edildi; hatalar düzeltildi ve son sürüm geri bildirimlere göre şekillendi
- Uygulamada kaybolmamak için kullanım kılavuzu

## Ekranlar

<p>
<img src="images/saya-1.jpg" width="200" alt="Giriş ekranı" />
<img src="images/saya-2.jpg" width="200" alt="Kayıt ekranı" />
<img src="images/saya-3.jpg" width="200" alt="Şifremi unuttum ekranı" />
</p>

## Nasıl çalışıyor

- **Veri:** ayrı bir sunucu yok. Kayıt bilgileri Google Form üzerinden Google E-Tablolar'a yazılıyor, uygulama da tabloyu App Inventor'ın Web bileşeniyle geri okuyor.
- **Giriş:** e-posta trim ve küçük harfle normalize edilip şifreyle birlikte tablodaki satırlarla eşleştiriliyor. Eşleşen satırın indeksi oturum boyunca tutuluyor.
- **Kayıt:** boş alan, e-posta formatı, daha önce kayıtlı e-posta, KVKK onayı ve yaş onayı kontrol ediliyor. Boy, kilo ve üç gizli soru alınıyor.
- **Günlük puan:** ana ekranda besin grupları (su, süt-yoğurt, yumurta, tahıl, sebze, kuruyemiş-meyve, kırmızı et, şarküteri, sıvı yağ, cips-çikolata), kahvaltı, aktivite süresi ve ekran süresi için seçimler var. Her biri günün SAYA puanını artırıyor ya da azaltıyor.
- **Profil:** kayıtlı boy ve kiloyla BKİ hesaplanıp günlük grafiğe çiziliyor ve zayıf / normal / fazla kilolu / obez / morbid obez olarak etiketleniyor.

![BKİ grafiği blokları](images/saya-blocks.png)

Geriye dönüp bakınca zayıf nokta güvenlik: şifreler tabloda duruyor ve şifremi unuttum ekranı şifreyi açıkça gösteriyor. Bugün olsa Firebase Authentication kullanır, veriyi Firestore'da tutardım.

## Teknolojiler

MIT App Inventor 2, Android

## Rolüm

Danışman: öğrencilere tasarım, kodlama ve test sürecinde rehberlik ettim.

## Sonuç

Ortaokullar arası proje yarışmasında Türkiye 3.lüğü (2023).

---

Kaynak kod özel. İstenirse demo gösterebilir ya da kodu birlikte inceleyebiliriz.

[← Profile dön](../README.tr.md)
