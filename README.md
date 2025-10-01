🚀 Ad-Soyad Ayırıcı Uygulaması: Veri Düzenlemede Yeni Standart

Link: https://ad-soyad-ayirici.streamlit.app/

1. Giriş
Günümüz veri yönetimi süreçlerinde, ad ve soyad bilgilerinin tek bir sütunda bulunması (örneğin müşteri listeleri veya kayıt formları), raporlama ve sistem entegrasyonlarında ciddi zorluklar yaratır. Bu problemi çözmek ve veri işleme verimliliğini artırmak amacıyla, basit, hızlı ve çok formatlı bir araç geliştirilmiştir: Ad-Soyad Ayırıcı Uygulaması.

2. Problemler ve Neden Bu Uygulama?
Kurumsal veri setlerindeki temel sorun, ad ve soyadların tek bir sütunda birleşik olmasıdır. Bu durum:

Raporlama Zorlukları: Ad veya soyad bazlı hızlı filtreleme ve analiz yapmayı imkansız hale getirir.

Sistem Entegrasyonu: CRM, ERP veya E-ticaret sistemlerinin talep ettiği ayrı alanlara veri aktarımını karmaşıklaştırır.

Manuel Yük: Binlerce satırlık verinin elle düzenlenmesi ciddi zaman kaybına ve insan hatasına neden olur.

Bu uygulama, veriyi milisaniyeler içinde ayrıştırarak bu sorunları kökten çözer.

3. Çözüm ve Temel Özellikler
Uygulama, Python ve Streamlit teknolojileriyle geliştirilmiş, web tabanlı bir veri düzenleme aracıdır.

✨ Yeni Vurgulanan Özellikler (Güncelleme)
Özellik	Açıklama
Çoklu Giriş/Çıkış Desteği	Artık sadece Excel ve CSV değil, JSON (.json) dosyalarını da okuyabilir ve çıktı olarak verebilir.
Cloud Uyumlu Yapı	Streamlit Cloud gibi sunucusuz ortamlarda sorunsuz çalışır. Dosyayı yerel diske kaydetme yerine, düzenlenmiş veriyi doğrudan indirme butonu aracılığıyla kullanıcıya sunar.
Türkçe Karakter Desteği	JSON ve CSV kaydetme işlemlerinde Türkçe karakterlerin (Ç, Ğ, Ö, Ş, İ, Ü) hatasız görünmesi sağlanmıştır.

E-Tablolar'a aktar
🛠️ Mevcut Temel Özellikler
Dosya Yükleme: Kullanıcı, cihazından .xlsx, .csv, veya .json dosyalarını yükleyebilir.

Kolon Otomatik Algılama: Program, başlık adlarında (adsoyad, name surname, ad_soyad vb.) bulunan yaygın varyasyonları otomatik olarak tespit eder.

Hızlı Ayrıştırma: Veri setinin boyutuna bağlı olarak işlem süresi ekranda gösterilir ve ayrıştırma işlemi saniyeler sürer.

Esnek Ayrıştırma Algoritması: Adı birden fazla kelimeden oluşan (örneğin "Ayşe Nur Yılmaz") kayıtlar için ilk kelimeler "Ad" olarak birleştirilir, son kelime daima "Soyad" olarak atanır.

4. Teknik Altyapı ve Algoritma
⚙️ Kullanılan Teknolojiler
Teknoloji	Amaç
Python	Temel programlama dili.
Pandas	Veri setlerini okuma, işleme, manipülasyon ve çıktı alma (Excel, CSV, JSON) için.
Streamlit	Hızlı ve kullanıcı dostu arayüz oluşturma.
io Kütüphanesi	Streamlit Cloud ortamında dosya işlemlerini bellek üzerinde (in-memory) gerçekleştirmek için (sunucuya kaydetme zorunluluğunu ortadan kaldırır).

E-Tablolar'a aktar
🧠 Ayrıştırma Algoritmasının İşleyişi
Girdi: Yüklenen dosyanın uzantısı belirlenir ve Pandas ile DataFrame olarak okunur.

Sütun Tespiti: Tanımlı başlık listesi taranarak tek birleşik ad-soyad sütunu bulunur.

Ayrıştırma (Örnekler):

"Ali Yılmaz" → Ad: Ali, Soyad: Yılmaz

"Ayşe Nur Kara" → Ad: Ayşe Nur, Soyad: Kara

"Deniz" → Ad: Deniz, Soyad: (Boş)

Çıktı: Yeni 'Ad' ve 'Soyad' sütunları eklenmiş DataFrame, seçilen formatta (Excel, CSV veya JSON) bellekte oluşturulur ve kullanıcıya indirilmek üzere sunulur.

5. Kullanım Senaryoları
Kurumsal Veri Yönetimi: Personel, müşteri veya tedarikçi listelerinin temizlenmesi.

Eğitim Sektörü: Öğrenci kayıt sistemlerine toplu veri girişi öncesi verilerin standartlaştırılması.

Pazarlama ve E-ticaret: Kullanıcı verilerinin CRM veya E-posta Pazarlama sistemlerine hızlı entegrasyonu.

Araştırma: Anket ve form sonuçlarından elde edilen veri setlerinin analize hazırlanması.

6. Sonuç ve Projenin Katkısı
Ad-Soyad Ayırıcı Uygulaması, basit bir ihtiyacı modern teknolojilerle çözerek, veri temizleme sürecini saniyelerle ifade edilen bir otomasyona dönüştürür. Hız, doğruluk ve güncel JSON formatı desteği sayesinde veri yönetimi süreçlerinize doğrudan katma değer sağlar.

"İhtiyaçtan doğan yazılımlar, iş yükünü azaltır, verimliliği artırır."
