import os
import io # Bellek içi (in-memory) dosya işlemleri için
import json # JSON işlemleri için (CSV okuma döngüsü için gerekli olabilir)

# === Ad-Soyad Ayırıcı Fonksiyon ===
def split_name(full_name):
    parts = full_name.strip().split()
    if len(parts) == 1:
        return parts[0], ""
    elif len(parts) == 2:
        return parts[0], parts[1]
    else:
        # İki veya daha fazla kelimesi olanları Ad ve Soyad olarak ayırır
        return " ".join(parts[:-1]), parts[-1]

# === Geçerli başlık isimleri ===
possible_columns = [
    "adsoyad", "ad soyad", "ad_soyad",
    "namesurname", "name surname", "name_surname",
    "adsurname", "ad surname"
]

# === Streamlit Arayüzü ===
st.set_page_config(page_title="Ad-Soyad Düzenleyici", layout="centered")
st.title("📄 Ad-Soyad Düzenleyici (Excel, CSV ve JSON)")

st.markdown("""
Bu uygulama **Excel (.xlsx)**, **CSV (.csv)** veya **JSON (.json)** dosyalarındaki ad-soyad sütununu ayırır.
1️⃣ Dosyanızı yükleyin
2️⃣ **Çıktı dosya türünü** seçin
3️⃣ "İşlemi Başlat" butonuna tıklayın
""")

# JSON dosya türünü ekliyoruz
uploaded_file = st.file_uploader("Dosyanızı yükleyin", type=["xlsx", "csv", "json"])

if uploaded_file:

    # JSON çıktı formatını ekliyoruz
    output_format = st.radio(
        "Kaydedilecek dosya türünü seçin:",
        options=["Excel (.xlsx)", "CSV (.csv)", "JSON (.json)"]
    )

    if st.button("🚀 İşlemi Başlat"):
        start_time = time.time()
        df = None # df'yi try bloğu dışında tanımlıyoruz
        
        try:
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()

            # --- Dosya Okuma ---
            if file_ext == ".xlsx":
                df = pd.read_excel(uploaded_file)

            elif file_ext == ".json":
                # JSON okuma: uploaded_file'dan doğrudan okuyup DataFrame'e çeviriyoruz
                df = pd.read_json(uploaded_file)
            
            elif file_ext == ".csv":
                # Mevcut CSV otomatik algılama mantığı
                for encoding in ["utf-8", "ISO-8859-9", "latin1"]:
                    for sep in [",", ";", "|", "\t"]:
                        try:
                            uploaded_file.seek(0)
                            temp_df = pd.read_csv(uploaded_file, encoding=encoding, sep=sep)
                            if not temp_df.empty:
                                df = temp_df
                                break
                        except Exception:
                            continue
                    if df is not None:
                        break

            # --- Dosya Kontrolü ---
            if df is None or df.empty:
                st.error("❌ Dosya okunamadı. Dosya boş olabilir veya format/kodlama hatalı.")
                st.stop()
            
            # --- Sütun Bulma ---
            matched_col = None
            for col in df.columns:
                if col.strip().lower() in possible_columns:
                    matched_col = col
                    break

            if not matched_col:
                st.error(f"Dosyada uygun bir ad-soyad sütunu bulunamadı!\nAranan başlıklar: {possible_columns}")
                st.stop()

            # --- Ad-Soyad Ayırma ---
            # NaN değerler veya hatalı girdiler için str() kullanmak güvenlidir
            df[['Ad', 'Soyad']] = df[matched_col].astype(str).apply(lambda x: pd.Series(split_name(x)))

            # --- Çıktı Dosyası İşlemleri ---
            output_buffer = io.BytesIO() # Bellek tamponu
            
            if "Excel" in output_format:
                output_ext = ".xlsx"
                df.to_excel(output_buffer, index=False)
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            elif "CSV" in output_format:
                output_ext = ".csv"
                df.to_csv(output_buffer, index=False, encoding="utf-8")
                mime_type = "text/csv"
            
            elif "JSON" in output_format:
                output_ext = ".json"
                # JSON çıktısı için 'orient' parametresi genellikle 'records' veya 'split' kullanılır
                df.to_json(output_buffer, orient="records", indent=4, force_ascii=False)
                mime_type = "application/json"
                
            output_buffer.seek(0) # İmleci başlangıca taşı

            elapsed_time = round(time.time() - start_time, 2)

            # --- Sonuç ve İndirme ---
            st.success(f"✅ İşlem tamamlandı! Düzenlenen kayıt sayısı: **{len(df)}**")
            st.info(f"⏱ İşlem süresi: **{elapsed_time} saniye**")

            st.download_button(
                label="📥 Düzenlenmiş Dosyayı İndir",
                data=output_buffer,
                file_name="ad_soyad_duzeltilmis" + output_ext,
                mime=mime_type
            )

        except Exception as e:
            st.error(f"❌ Hata oluştu: {e}")

else:
    st.warning("Lütfen bir dosya yükleyin ve çıktı türünü seçin.")




