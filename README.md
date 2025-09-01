# Ad-Soyad-Ayirici

İhtiyaçtan Doğan Bir Program: Ad-Soyad Ayırıcı Uygulaması

1. Giriş

Günümüz dijital çağında veri işleme ve düzenleme ihtiyacı her geçen gün artmaktadır. Özellikle müşteri listeleri, öğrenci kayıtları, personel tabloları veya resmi belgelerde ad ve soyad bilgilerinin ayrı sütunlarda tutulması hem analiz süreçlerini kolaylaştırmakta hem de sistemsel entegrasyonlarda hataları azaltmaktadır.
Bu noktada ortaya çıkan ihtiyaç, basit ama etkili bir çözümü doğurdu: Ad-Soyad Ayırıcı Programı.

2. Problemin Tanımı

Kurumsal veri setlerinin çoğunda ad ve soyad bilgileri tek bir sütunda bulunur. Bu durum, aşağıdaki sorunlara yol açar:

Raporlama zorlukları: Ad ve soyad bazlı analiz yapmak zorlaşır.

CRM veya ERP entegrasyonu: Ad ve soyad için ayrı alanlar talep eden sistemlere veri aktarımı karmaşıklaşır.

Manuel düzenleme yükü: Binlerce satırdan oluşan dosyaların elle ayrıştırılması ciddi zaman kaybına neden olur.

İşte bu problemleri çözmek için pratik, hızlı ve kullanıcı dostu bir araç geliştirilmiştir.

3. Çözüm: Ad-Soyad Ayırıcı Uygulaması

Program, Python ve Streamlit teknolojileriyle geliştirilmiş, hem Excel (.xlsx) hem de CSV dosyaları üzerinde çalışan, kolay kullanımlı bir masaüstü web uygulamasıdır.

3.1. Temel Özellikler

Dosya yükleme: Kullanıcı, cihazından bir Excel veya CSV dosyası yükleyebilir.

Kolon otomatik algılama: Program, başlık adlarında “Ad Soyad”, “Name Surname”, “adsoyad” gibi varyasyonları otomatik olarak algılar.

Hızlı ayrıştırma: Binlerce satır veri milisaniyeler içinde ad ve soyad olarak iki sütuna ayrılır.

Kayıt imkanı: İşlenen dosya, kullanıcı tarafından seçilen konuma kaydedilebilir.

İşlem süresi gösterimi: Kullanıcı, işlemin ne kadar sürede tamamlandığını ekranda görebilir.

4. Teknik Altyapı
4.1. Kullanılan Teknolojiler

Python: Temel programlama dili.

Pandas: Veri işleme ve düzenleme için.

Streamlit: Basit ve hızlı bir kullanıcı arayüzü sağlamak için.

4.2. Algoritmanın İşleyişi

Dosya yüklenir.

Kolon başlıkları taranır; ad-soyad içeren sütun otomatik tespit edilir.

Veriler satır satır ayrıştırılır:

Tek kelime: Ad alanına yazılır, soyad boş kalır.

İki kelime: İlk kelime ad, ikinci kelime soyad olarak ayrılır.

İkiden fazla kelime: İlk kısımlar ad olarak birleştirilir, son kelime soyad olur.

Yeni tablo oluşturulur.

İşlenmiş dosya kullanıcı tarafından seçilen konuma kaydedilir.

5. Kullanım Senaryoları

Kurumsal veri düzenleme: Personel veya müşteri listelerinin ayrıştırılması.

Eğitim sektörü: Öğrenci bilgilerini sisteme yükleme öncesi düzenleme.

Araştırma ve analiz: Anket sonuçlarındaki ad-soyad verilerinin temizlenmesi.

E-ticaret: Kullanıcı verilerinin CRM sistemlerine entegre edilmesi.

6. Kullanıcı Dostu Tasarım

Proje, teknik bilgisi olmayan kullanıcıların da rahatça kullanabilmesi için minimalist bir arayüzle tasarlanmıştır:

Dosya yükleme butonu

Kayıt konumu seçici

İşlem süresi göstergesi

Başarılı işlem sonrası otomatik indirme bağlantısı

7. Sonuç ve Katkılar

Bu proje, basit bir ihtiyacın doğru analiz edilmesi ve doğru teknolojilerle çözülmesi sayesinde, veri düzenleme süreçlerinde büyük zaman tasarrufu sağlamaktadır.

Hız: Manuel işlemlere göre yüzlerce kat daha hızlı.

Doğruluk: İnsan hatasını ortadan kaldırır.

Esneklik: Hem Excel hem CSV desteği sayesinde farklı senaryolara uyarlanabilir.

8. Son Söz

“İhtiyaçtan doğan yazılımlar”, sadece teknik bir çözüm değil, aynı zamanda gerçek hayat problemlerine yönelik pratik bir yardım aracıdır. Ad-Soyad Ayırıcı Programı, veri yönetimini kolaylaştıran, zaman kazandıran ve kullanıcı dostu yapısıyla tam da bu felsefeyi yansıtan bir projedir.
