Türkçe | [English](akilli-asansor.md)

# Akıllı Asansör

Standart asansör panelini kullanmakta zorlanan kişiler için sesle, işaretle ya da düğmeyle çağrılabilen bir asansör modeli.

## Nedir

Arduino ile kontrol edilen bir asansör modeli. MIT App Inventor uygulaması kat komutunu Bluetooth (HC-06) ile gönderiyor, Arduino UNO da L298N sürücü üzerinden DC motoru çalıştırıyor. Benim danışmanlığımda bir ortaokul öğrencisiyle geliştirildi.

## Nasıl çalışıyor

- `0`-`4` komutları kabini o kata gönderiyor, `5` durduruyor
- Motor birden tam hıza çıkmak yerine PWM ile hızlanıp yavaşlıyor
- İkinci sürümde fiziksel kat düğmeleri ve 7 segment gösterge var
- Bluetooth, motor ve ses tanıma modülü için ayrı deneme kodları
- Kabin Tinkercad'de modellendi

## Teknolojiler

Arduino (C++), HC-06 Bluetooth, L298N, MIT App Inventor 2, Tinkercad

## Rolüm

Danışman ve geliştirici: yazılımı öğrenciyle birlikte yazdım, tasarım ve test sürecinde rehberlik ettim.

## Sonuç

TÜBİTAK 2204-B · İzmir bölge 3.lüğü, 2022.

---

Kaynak kod özel. İstenirse demo gösterebilir ya da kodu birlikte inceleyebiliriz.

[← Profile dön](../README.tr.md)
