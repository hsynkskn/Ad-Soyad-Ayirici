import streamlit as st
import pandas as pd
import time
import os

# === Ad-Soyad Ayırıcı Fonksiyon ===
def split_name(full_name):
    parts = full_name.strip().split()
    if len(parts) == 1:
        return parts[0], ""
    elif len(parts) == 2:
        return parts[0], parts[1]
    else:
        return " ".join(parts[:-1]), parts[-1]

# === Geçerli başlık isimleri ===
possible_columns = [
    "adsoyad", "ad soyad", "ad_soyad",
    "namesurname", "name surname", "name_surname",
    "adsurname", "ad surname"
]

# === Streamlit Arayüzü ===
st.set_page_config(page_title="Ad-Soyad Düzenleyici", layout="centered")
st.title("📄 Ad-Soyad Düzenleyici (Excel ve CSV)")

st.markdown("""
Bu uygulama **Excel (.xlsx)** veya **CSV (.csv)** dosyalarındaki ad-soyad sütununu ayırır.  
1️⃣ Dosyanızı yükleyin  
2️⃣ Kayıt konumunu ve **çıktı dosya türünü** seçin  
3️⃣ "İşlemi Başlat" butonuna tıklayın  
""")

uploaded_file = st.file_uploader("Dosyanızı yükleyin", type=["xlsx", "csv"])

# Kayıt klasörleri
folders = [
    os.getcwd(),
    r"~\Desktop",
    r"~\Downloads",
    r"~\Documents"
] 
save_folder = st.selectbox("Düzenlenmiş dosyayı kaydedeceğiniz konumu seçin:", folders)

# Çıktı türü seçimi
output_format = st.radio(
    "Kaydedilecek dosya türünü seçin:",
    options=["Excel (.xlsx)", "CSV (.csv)"]
)

if uploaded_file and save_folder:
    if st.button("🚀 İşlemi Başlat"):
        start_time = time.time()
        try:
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()

            # === Dosya okuma ===
            if file_ext == ".xlsx":
                df = pd.read_excel(uploaded_file)

            elif file_ext == ".csv":
                df = None
                for encoding in ["utf-8", "ISO-8859-9", "latin1"]:
                    for sep in [",", ";", "|", "\t"]:
                        try:
                            uploaded_file.seek(0)  # Dosya imlecini sıfırla
                            temp_df = pd.read_csv(uploaded_file, encoding=encoding, sep=sep)
                            if not temp_df.empty:
                                df = temp_df
                                break
                        except Exception:
                            continue
                    if df is not None:
                        break

                if df is None or df.empty:
                    st.error("❌ CSV dosyası okunamadı. Dosya boş olabilir veya ayırıcı/kodlama hatalı.")
                    st.stop()
            else:
                st.error("❌ Desteklenmeyen dosya formatı!")
                st.stop()

            # === Sütun bulma ===
            matched_col = None
            for col in df.columns:
                if col.strip().lower() in possible_columns:
                    matched_col = col
                    break

            if not matched_col:
                st.error(f"Dosyada uygun bir ad-soyad sütunu bulunamadı!\nAranan başlıklar: {possible_columns}")
                st.stop()

            # === Ad-Soyad ayırma ===
            df[['Ad', 'Soyad']] = df[matched_col].apply(lambda x: pd.Series(split_name(str(x))))

            # === Çıktı dosyası uzantısı ===
            if "Excel" in output_format:
                output_ext = ".xlsx"
            else:
                output_ext = ".csv"

            output_path = os.path.join(save_folder, "ad_soyad_duzeltilmis" + output_ext)

            # === Kaydetme ===
            if output_ext == ".xlsx":
                df.to_excel(output_path, index=False)
            else:
                df.to_csv(output_path, index=False, encoding="utf-8")

            elapsed_time = round(time.time() - start_time, 2)

            st.success(f"✅ İşlem tamamlandı! Dosya kaydedildi:\n`{output_path}`")
            st.info(f"⏱ İşlem süresi: **{elapsed_time} saniye**")

            with open(output_path, "rb") as f:
                st.download_button(
                    label="📥 Düzenlenmiş Dosyayı İndir",
                    data=f.read(),
                    file_name="ad_soyad_duzeltilmis" + output_ext
                )

        except Exception as e:
            st.error(f"❌ Hata oluştu: {e}")

else:
    st.warning("Lütfen bir dosya yükleyin, kayıt konumunu ve çıktı türünü seçin.")



