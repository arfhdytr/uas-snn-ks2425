import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Pembahasan SNN", 
    page_icon="📊", 
    layout="wide"
)

# Kustomisasi CSS sedikit untuk mempertegas UI agar rapi (mendukung Antislop C-1)
st.markdown("""
<style>
    .stMetric {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    .explanation {
        background-color: #fef3c7;
        border-left: 4px solid #d97706;
        padding: 1rem;
        border-radius: 6px;
        color: #92400e;
        margin-bottom: 1rem;
    }
    .question-box {
        background-color: #e0f2fe;
        border-left: 4px solid #0284c7;
        padding: 1rem;
        border-radius: 6px;
        color: #0f172a;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- TOP NAVBAR (TABS) -----------------
st.title("📚 Pembahasan & Materi SNN")

tab_materi, tab_22, tab_23, tab_24 = st.tabs(["Materi", "Soal 22/23", "Soal 23/24", "Soal 24/25"])

# ----------------- KONTEN MENU -----------------
with tab_materi:
    st.header("Materi Perkuliahan SNN")
    
    st.markdown("""
    <div class="explanation">
        Materi ini dirangkum berdasarkan dokumen pembelajaran SNN, mencakup konsep dasar PDB, pendekatan perhitungannya, hingga metode analisis makroekonomi yang diturunkan dari data PDB/PDRB.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("1. Konsep Penilaian PDB")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="stMetric">
        <strong>PDB Atas Dasar Harga Berlaku (ADHB / Nominal)</strong><br>
        Dihitung berdasarkan harga pasar aktual pada tahun berjalan.<br>
        <ul>
            <li>Menggambarkan struktur transaksi moneter riil.</li>
            <li>Nilainya rentan mengalami distorsi oleh kenaikan harga (inflasi).</li>
            <li><strong>Kegunaan:</strong> Analisis rasio keuangan makro (rasio pajak, defisit anggaran APBN terhadap PDB, dan daya serap investasi aktual).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stMetric">
        <strong>PDB Atas Dasar Harga Konstan (ADHK / Riil)</strong><br>
        Dihitung dengan mengacu pada indeks harga tetap pada satu Tahun Dasar.<br>
        <ul>
            <li>Menghilangkan unsur perubahan harga pasar.</li>
            <li>Murni mencerminkan peningkatan volume fisik produksi riil di lapangan.</li>
            <li><strong>Kegunaan:</strong> Laju pertumbuhan ekonomi, efektivitas kebijakan fiskal, dan evaluasi produktivitas sektoral.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("2. PDB Berdasarkan 3 Pendekatan")

    tab_prod, tab_peng, tab_pend = st.tabs(["Pendekatan Produksi", "Pendekatan Pengeluaran", "Pendekatan Pendapatan"])

    with tab_prod:
        st.markdown("#### PDB Pendekatan Produksi")
        st.write("PDB adalah penjumlahan nilai tambah atas barang dan jasa yang dihasilkan oleh berbagai unit produksi di wilayah suatu negara dalam jangka waktu tertentu.")
        st.info("**Nilai Tambah Bruto (NTB)** = Output - Konsumsi Antara\n\n**PDB/PDRB** = Total NTB + Pajak Atas Produk - Subsidi Atas Produk")
        
        with st.expander("17 Kategori Lapangan Usaha (KBLI)"):
            st.markdown("""
            1. **A.** Pertanian, Kehutanan, dan Perikanan
            2. **B.** Pertambangan dan Penggalian
            3. **C.** Industri Pengolahan
            4. **D.** Pengadaan Listrik dan Gas
            5. **E.** Pengadaan Air, Pengelolaan Sampah, Limbah dan Remediasi
            6. **F.** Konstruksi
            7. **G.** Perdagangan Besar dan Eceran; Reparasi Mobil dan Sepeda Motor
            8. **H.** Transportasi dan Pergudangan
            9. **I.** Penyediaan Akomodasi dan Makan Minum
            10. **J.** Informasi dan Komunikasi
            11. **K.** Jasa Keuangan dan Asuransi
            12. **L.** Real Estat
            13. **M,N.** Jasa Perusahaan
            14. **O.** Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib
            15. **P.** Jasa Pendidikan
            16. **Q.** Jasa Kesehatan dan Kegiatan Sosial
            17. **R,S,T,U.** Jasa Lainnya
            """)
        st.warning("**Catatan Penting:**\n- PDB hanya menghitung nilai *final goods* (menghindari *double counting*), bukan *intermediate goods*.\n- PDB tidak menghitung transaksi *financial asset* (saham, obligasi).\n- PDB tidak menghitung penjualan barang bekas (hanya barang yang diproduksi saat ini).\n- Barang tanpa nilai pasar dihitung menggunakan nilai estimasi (*imputed value*).")

    with tab_peng:
        st.markdown("#### PDB Pendekatan Pengeluaran")
        st.write("PDB adalah semua komponen permintaan akhir yang terdiri dari konsumsi, investasi, pengeluaran pemerintah, dan ekspor neto.")
        st.info("**PDB = C + I + G + (X - M)**\n\n*(Konsumsi RT + Investasi/PMTB + Konsumsi Pemerintah + Ekspor Neto)*")
        
        with st.expander("1. Pengeluaran Konsumsi Rumah Tangga (PK-RT)"):
            st.write("Pengeluaran rumah tangga untuk semua barang dan jasa (penggunaan akhir). Diklasifikasikan berdasarkan COICOP (12 divisi, spt makanan, pakaian, perumahan). Mencakup transaksi moneter (pembelian) dan non-moneter (barter, produksi dikonsumsi sendiri). Tidak termasuk pembelian aset rumah (masuk PMTB) dan barang berharga.")
        with st.expander("2. Pengeluaran Konsumsi LNPRT"):
            st.write("Lembaga Non-Profit yang Melayani Rumah Tangga (Ormas, Partai Politik, Lembaga Keagamaan, Serikat Buruh). Outputnya adalah output non-pasar, dihitung dari total biaya produksi = Biaya Antara + Kompensasi Pegawai + Penyusutan + Pajak.")
        with st.expander("3. Pengeluaran Konsumsi Pemerintah (PK-P)"):
            st.write("Biaya yang dikeluarkan pemerintah untuk menyediakan barang/jasa publik. Dibagi menjadi konsumsi kolektif (pertahanan/keamanan) dan individu (pendidikan/kesehatan).")
        with st.expander("4. Pembentukan Modal Tetap Bruto (PMTB) / Investasi"):
            st.write("Penambahan dikurangi pengurangan aset tetap (aset diproduksi dan digunakan berulang kali >1 tahun). Terdiri dari: Bangunan, Mesin, Kendaraan, *Cultivated Biological Resources* (tanaman/hewan jangka panjang), dan Produk Kekayaan Intelektual (software, eksplorasi mineral, *research & development*).")
        with st.expander("5. Perubahan Inventori"):
            st.write("Nilai produk yang masuk inventori dikurangi yang diambil dari inventori. Terdapat 5 jenis: Bahan baku/penolong, *Work in Progress* (barang setengah jadi), Barang jadi, Barang untuk dijual kembali, dan Inventori militer (amunisi).")
        with st.expander("6. Ekspor Neto (Ekspor - Impor)"):
            st.write("Transaksi alih kepemilikan ekonomi barang/jasa antara residen dan non-residen. Ekspor dinilai secara *f.o.b* (Free on Board) dan Impor dinilai *c.i.f* (Cost, Insurance, Freight). Termasuk aktivitas *merchanting* (beli dari luar negeri, dijual langsung ke luar negeri tanpa masuk wilayah domestik).")

    with tab_pend:
        st.markdown("#### PDB Pendekatan Pendapatan")
        st.write("PDB merupakan penjumlahan balas jasa faktor-faktor produksi milik residen dan non-residen di wilayah domestik.")
        st.info("**Pendapatan Nasional** = PDB Pendapatan - Net Factor Income (Pendapatan neto faktor produksi dari luar negeri)\n\n*(Pendapatan Nasional menghitung balas jasa milik warga negara sendiri baik di dalam maupun luar negeri).*")
        st.markdown("**Komponen Balas Jasa (Neraca Pendapatan Yang Dihasilkan):**")
        st.markdown("""
        - **Kompensasi Pegawai:** Total pendapatan baik *cash* maupun *in-kind* (barang/jasa) yang dibayarkan ke karyawan.
        - **Pajak Produksi & Impor (dikurangi Subsidi):** Pajak atas barang/jasa yang diproduksi (tidak termasuk PPN).
        - **Konsumsi Modal Tetap (Penyusutan)**
        - **Surplus Usaha Neto / Pendapatan Campuran:** Item penyeimbang (*balancing item*). Disebut *mixed income* (pendapatan campuran) untuk usaha rumah tangga tidak berbadan hukum, karena upah pemilik tidak bisa dibedakan dengan laba usaha.
        """)

    st.markdown("---")
    st.subheader("3. Analisis PDB / PDRB")
    
    with st.expander("📈 1. Pertumbuhan Ekonomi & Indeks Implisit"):
        st.markdown("""
        - **Laju Pertumbuhan Ekonomi:** Dihitung dari **PDB ADH Konstan**. Menggambarkan kinerja/keberhasilan pembangunan fisik riil suatu daerah.
          $$r = \\frac{Y_t - Y_{t-1}}{Y_{t-1}} \\times 100\\%$$
          *(Keterangan: $Y_t$ = PDB ADHK periode ke-t)*
        - **Indeks Implisit (PDRB Deflator):** Rasio antara PDB Berlaku dan PDB Konstan. Berfungsi sebagai indikator tingkat inflasi (perubahan harga).
          $$I_t = \\frac{X_{it}}{Y_{it}} \\times 100$$
          *(Keterangan: $X_{it}$ = PDB ADHB, $Y_{it}$ = PDB ADHK)*
        - **Laju Indeks Implisit:**
          $$\\Delta I_t = \\left( \\frac{I_t}{I_{t-1}} \\times 100\\% \\right) - 100\\%$$
        """)

    with st.expander("🥧 2. Struktur Ekonomi & Sumber Pertumbuhan"):
        st.markdown("""
        - **Struktur Ekonomi (Kontribusi):** Diperoleh dari proporsi lapangan usaha terhadap Total **PDB ADH Berlaku**.
          $$\\text{Kontribusi Sektor}_i = \\frac{\\text{PDB ADHB}_i}{\\text{Total PDB ADHB}} \\times 100\\%$$
        - **Sumber Pertumbuhan Ekonomi (Source of Growth):** Seberapa besar sumbangan suatu sektor dalam menciptakan total laju pertumbuhan ekonomi wilayah.
          $$SOG_{it} = \\frac{y_{it} - y_{it-1}}{\\sum y_{it-1}} \\times 100\\%$$
          *(Keterangan: $y_{it}$ = PDB ADHK sektor ke-i pada tahun ke-t, penyebut adalah Total PDB ADHK tahun sebelumnya)*
        """)

    with st.expander("📍 3. Location Quotient (LQ) & Shift Share"):
        st.markdown("""
        - **Location Quotient (LQ):** Menentukan derajat *self-sufficiency* dan kapasitas ekspor perekonomian daerah. 
          $$LQ = \\frac{v_i / v_t}{V_i / V_t}$$
          *(Keterangan: $v_i$ = PDRB sektor $i$ daerah, $v_t$ = Total PDRB daerah, $V_i$ = PDB sektor $i$ nasional, $V_t$ = Total PDB nasional)*
          - `LQ > 1`: Sektor **Basis** (mampu diekspor).
          - `LQ <= 1`: Sektor **Non-Basis** (butuh impor).
        - **Analisis Shift Share (SS):** Menganalisis transformasi struktur ekonomi wilayah.
          $$\\Delta y_i = y_i^0 \\left(\\frac{Y^t}{Y^0} - 1\\right) + y_i^0 \\left(\\frac{Y_i^t}{Y_i^0} - \\frac{Y^t}{Y^0}\\right) + y_i^0 \\left(\\frac{y_i^t}{y_i^0} - \\frac{Y_i^t}{Y_i^0}\\right)$$
          *(Suku 1 = Regional Share, Suku 2 = Proportional Shift, Suku 3 = Differential Shift)*
        """)

    with st.expander("📊 4. Tipologi Klassen & Indeks Williamson"):
        st.markdown("""
        - **Tipologi Klassen:** Klasifikasi daerah dalam 4 kuadran berdasarkan Laju Pertumbuhan dan PDRB Per Kapita dibanding daerah acuan (nasional).
        - **Indeks Williamson:** Mengetahui ketimpangan/kesenjangan distribusi pendapatan antar daerah.
          $$I_w = \\frac{\\sqrt{\\sum (y_i - \\bar{y})^2 (f_i/n)}}{\\bar{y}}$$
          *(Keterangan: $y_i$ = PDRB perkapita daerah i, $\\bar{y}$ = PDRB perkapita semua daerah, $f_i$ = penduduk daerah i, $n$ = total penduduk)*
        - **Indeks Bonet:**
          $$IB_i = \\frac{\\text{PDRB perkapita}_i}{\\text{PDRB perkapita}_{reference}} - 1$$
        """)

    with st.expander("⚙️ 5. Analisis Makro Lainnya (ICOR, Elastisitas TK, MPC, PDRB Perkapita)"):
        st.markdown("""
        - **PDRB Per Kapita:** Indikator dasar kesejahteraan dan produktivitas masyarakat.
          $$\\text{PDRB Per Kapita} = \\frac{\\text{PDRB}}{\\text{Total Penduduk}}$$
        - **ICOR (Incremental Capital Output Ratio):** Menunjukkan efisiensi investasi.
          $$ICOR = \\frac{\\Delta I}{\\Delta Y}$$
        - **Elastisitas Tenaga Kerja:** Menunjukkan seberapa padat karya pertumbuhan ekonomi.
          $$E_{TK} = \\frac{\\Delta TK / TK}{\\Delta Y / Y}$$
        - **MPC (Marginal Propensity to Consume):** Bagian dari tambahan pendapatan yang dialokasikan untuk konsumsi.
          $$MPC = \\frac{\\Delta C}{\\Delta Y_d}$$
        - **APC (Average Propensity to Consume):** Bagian dari pendapatan yang dialokasikan untuk konsumsi.
          $$APC = \\frac{C}{Y_d}$$
        """)

with tab_22:
    st.header("Pembahasan UAS SNN 2022/2023")
    
    with st.expander("Soal 1: Konsep & Analisis PDB", expanded=True):
        st.markdown("""
        **Pertanyaan:**
        a. Jelaskan mengapa PDB disajikan dalam atas dasar harga konstan dan atas dasar harga berlaku?
        b. Jelaskan bagaimana PDB dapat digunakan untuk menganalisis perbandingan antar wilayah.
        c. Jelaskan bagaimana PDB dapat digunakan untuk menganalisis perekonomian antar waktu dan antar komponen penyusunnya.

        **Pembahasan:**
        a. **PDB ADHB** (Harga Berlaku) digunakan untuk melihat pergeseran dan struktur ekonomi, sedangkan **PDB ADHK** (Harga Konstan) digunakan untuk mengetahui pertumbuhan ekonomi riil dari tahun ke tahun karena sudah bebas dari efek inflasi.
        b. **Analisis Antar Wilayah:** Dapat dilakukan dengan membandingkan nilai PDB (menunjukkan kapasitas ekonomi), PDB per kapita (tingkat kesejahteraan), laju pertumbuhan (potensi masa depan), Indeks Williamson/Bonet (kesenjangan), *Location Quotient* (sektor basis), dan Tipologi Klassen.
        c. **Analisis Antar Waktu & Komponen:** Dapat dilakukan dengan membandingkan nilai PDB dan per kapita dari tahun ke tahun untuk melihat laju pertumbuhan ekonomi. Selain itu, melihat sektor/lapangan usaha mana yang memiliki kontribusi (struktur) terbesar pada suatu titik waktu, dan bagaimana perubahannya seiring waktu.
        """)

    with st.expander("Soal 2: PDB Penggunaan & Diskrepansi"):
        st.markdown("""
        **Data PDB Penggunaan (Miliar Rp):**
        | Komponen | 2018 | 2019 |
        |---|---|---|
        | PK-RT | 8.274.214 | 8.965.837 |
        | PK-LNPRT | 180.893 | 206.094 |
        | PK-P | 1.338.639 | 1.394.615 |
        | PMTB | 4.791.211 | 5.121.371 |
        | Perubahan Inventori | 338.634 | 226.923 |
        | Ekspor | 3.116.546 | 2.943.533 |
        | Impor (pengurang) | 3.275.145 | 3.013.944 |
        | Diskrepansi Statistik | 73.764 | -11.773 |
        | **PDB** | **14.838.756** | **15.832.657** |

        **Pembahasan:**
        a. **Proporsi Penggunaan:** Proporsi mirip antara 2018 dan 2019. Penggunaan terbesar adalah PK-RT (tumbuh 8,36% di 2019). Terbesar kedua adalah PMTB (tumbuh 6,89%). PK-LNPRT mengalami pertumbuhan tertinggi (13,93%).
        b. **Diskrepansi Statistik:** Muncul karena adanya perbedaan metode, sumber data, dan waktu pencatatan antara perhitungan PDB pendekatan lapangan usaha dan PDB pendekatan pengeluaran yang seharusnya bernilai sama secara teoritis.
        c. **Elastisitas Konsumsi RT:** 
           - % Pertumbuhan PK-RT = 8,36%
           - % Pertumbuhan PDB (Pendapatan) = ((15.832.657 - 14.838.756) / 14.838.756) * 100% = 6,69%
           - Elastisitas = 8,36 / 6,69 = **1,25**
           *Interpretasi:* Tiap kenaikan PDB sebesar 1% akan meningkatkan pengeluaran konsumsi RT sebesar 1,25%.
        """)

    with st.expander("Soal 3: NTB Kedelai (ADHB & ADHK)"):
        st.markdown("""
        **Data Produksi Kedelai Negara Metapesta:**
        - **2017:** 70.000 ton, Harga Rp14.200/kg
        - **2018:** 85.000 ton, Harga Rp14.800/kg
        - **2019:** 92.000 ton, Harga Rp15.500/kg
        *(Rasio Biaya Antara 2017 & 2018 = 0,02; 2019 = 0,03)*

        **Pembahasan a. NTB ADHB (Harga Berlaku):**
        - **2017:** (70.000 * 14.200) - (0,02 * 70.000 * 14.200) = **Rp974.120.000**
        - **2018:** (85.000 * 14.800) - (0,02 * 85.000 * 14.800) = **Rp1.232.840.000**
        - **2019:** (92.000 * 15.500) - (0,03 * 92.000 * 15.500) = **Rp1.383.220.000**

        **Pembahasan b. NTB ADHK 2010 untuk 2017-2019:**
        *(Diasumsikan harga konstan 2010 sama dengan harga 2017 yaitu 14.200)*
        - **2017:** = **Rp974.120.000**
        - **2018:** (85.000 * 14.200) - (0,02 * 85.000 * 14.200) = **Rp1.182.860.000**
        - **2019:** (92.000 * 14.200) - (0,03 * 92.000 * 14.200) = **Rp1.267.208.000**

        **Pembahasan c. NTB ADHK 2020-2022 (Rasio biaya antara 0,03):**
        - Indeks Produksi (2010=100): 2020=220, 2021=235, 2022=252. Indeks Harga: 160, 172, 186.
        - **2020:** Produksi = 220.000, Harga = 22.720, Output = 4.998.400.000, NTB = **4.848.448.000**
        - **2021:** Produksi = 235.000, Harga = 24.424, Output = 5.739.640.000, NTB = **5.567.450.800**
        - **2022:** Produksi = 252.000, Harga = 26.412, Output = 6.655.824.000, NTB = **6.456.149.280**
        """)

    with st.expander("Soal 4: Analisis PDRB Provinsi Z"):
        st.markdown("""
        **Pertanyaan & Pembahasan:**
        a. **Indeks implisit konstruksi 2011=105, 2022=147. Artinya?**
           Terjadi kenaikan harga barang/jasa di tingkat produsen sektor konstruksi sebesar 5% pada tahun 2011, dan naik 47% pada tahun 2022 (keduanya dibandingkan tahun dasar 2010).
        
        b. **Sektor laju indeks implisit tertinggi di 2022?**
           Jasa Keuangan dan Asuransi (8,974%).
        
        c. **Bandingkan struktur ekonomi 2011 dan 2022.**
           Sektor unggulan tetap Industri Pengolahan. Namun kontribusinya menurun dari 14,4% di 2011 menjadi 11,9% di 2022 (turun 2,478%).
           
        d. **Bandingkan laju pertumbuhan Akomodasi Makan Minum dgn laju ekonomi Provinsi 2022.**
           - LPE Akomodasi = ((1638 - 1369)/1369) * 100% = **19,65%**
           - LPE Provinsi Z = ((16569 - 14937)/14937) * 100% = **10,92%**
           *Artinya:* Sektor akomodasi tumbuh jauh lebih cepat dibandingkan rata-rata perekonomian provinsi secara keseluruhan.
        """)

with tab_23:
    st.header("Pembahasan UAS SNN 2023/2024")
    
    with st.expander("Soal 1-4: Konsep Dasar PDB", expanded=True):
        st.markdown("""
        **1. Pendekatan Produksi & Alasan BPS Tidak Menggunakan Total Output**
        Pendekatan Produksi menjumlahkan Nilai Tambah Bruto (NTB) dari seluruh sektor. Total output tidak digunakan karena mengandung duplikasi (*double counting*), di mana produk suatu sektor menjadi input bagi sektor lain.
        
        **2. Komponen PDB Pengeluaran**
        $Y = C + I + G + (X - M)$. Terdiri dari Konsumsi Rumah Tangga (C), Pembentukan Modal Tetap Bruto/Investasi (I), Konsumsi Pemerintah (G), dan Ekspor Neto (X-M).
        
        **3. Pendekatan Pendapatan & Alasan BPS Tidak Menggunakannya**
        Menjumlahkan balas jasa faktor produksi (Upah, Sewa, Bunga, Laba, Pajak Neto). BPS tidak merilisnya sebagai PDB utama karena data tidak lengkap/akurat, banyak pendapatan non-moneter, dan risiko duplikasi sumber data.
        
        **4. Metode Harga Berlaku & 4 Metode Harga Konstan**
        Harga berlaku menggunakan harga tahun berjalan. Harga konstan menggunakan harga tahun dasar. 4 Metode Harga Konstan: 
        - Revaluasi
        - Ekstrapolasi
        - Deflasi Langsung (*Direct Deflation*)
        - Deflasi Ganda (*Double Deflation*)
        """)

    with st.expander("Soal 5: Analisis Fluktuasi Ekonomi"):
        st.markdown("""
        **a. Interpretasi Grafik LPE (Fluktuatif):**
        Pertumbuhan ekonomi belum stabil dan rentan tekanan eksternal/internal. Ekonomi tumbuh pesat di 2018, melambat drastis di 2020 akibat COVID-19, pulih di 2022, namun kembali terkontraksi di 2023.
        
        **b. Makna (1) Kenaikan Indeks Implisit, (2) Kenaikan SOG Industri Pengolahan:**
        1) Kenaikan Indeks Implisit menunjukkan terjadinya inflasi/kenaikan harga di tingkat produsen. Jika naik tajam, PDB Nominal membesar karena harga, bukan karena volume riil.
        2) Kenaikan SOG Industri Pengolahan menunjukkan sektor ini menjadi kontributor (motor pendorong) utama terhadap total persentase laju pertumbuhan ekonomi wilayah.
        """)

    with st.expander("Soal 6: Location Quotient (LQ) Kab. Berau"):
        st.markdown("""
        Data PDRB ADHK 2022 Provinsi Kaltim dan Kab. Berau.
        $$LQ = \\frac{\\text{PDRB Sektor } i \\text{ Berau} / \\text{Total PDRB Berau}}{\\text{PDRB Sektor } i \\text{ Kaltim} / \\text{Total PDRB Kaltim}}$$
        
        **Hasil LQ Sektor Berau:**
        - Pertanian = 1,38 (Basis)
        - Pertambangan = 1,36 (Basis)
        - Industri Pengolahan = 0,20 (Non-Basis)
        - Pengadaan Listrik = 0,43 (Non-Basis)
        *(Sektor yang memiliki LQ > 1 ditetapkan sebagai sektor Basis).*
        
        **Interpretasi:**
        Sektor basis (LQ > 1) seperti Pertanian dan Pertambangan mampu memenuhi kebutuhan lokal dan diekspor. Kabupaten Berau sangat bergantung pada sektor primer. Sementara sektor sekunder seperti Industri Pengolahan sangat lemah (LQ=0,20), yang mengindikasikan perlunya penguatan hilirisasi industri.
        """)

    with st.expander("Soal 7: Inazuma (APC, MPS, ICOR)"):
        st.markdown("""
        **Data Inazuma 2022-2023 (Miliar):**
        - PDRB 2022 = 1200 M, 2023 = 1320 M (Tumbuh 10%)
        - PK-P 2022 = 450 M, 2023 = 499,5 M (Naik 11%)
        - PMTB 2022 = 150 M, 2023 = 136 M
        - APC RT 2022 = 0,5
        - MPC RT 2023 = 0,7
        
        **a. Melengkapi Tabel PDRB Penggunaan:**
        - PK-RT 2022 = APC * PDRB = 0,5 * 1200 = 600 M
        - PK-RT 2023 = PK-RT 2022 + MPC * (PDRB 2023 - PDRB 2022) = 600 + 0,7*(120) = 684 M
        
        **b. APC 2023:**
        $$APC = \\frac{C}{Y} = \\frac{684}{1320} = 0,518$$
        *Artinya, di tahun 2023, masyarakat Inazuma menghabiskan sekitar 51,8% pendapatannya untuk konsumsi.*
        
        **c. MPS 2023:**
        $$MPS = 1 - MPC = 1 - 0,7 = 0,3$$
        *Artinya, setiap tambahan pendapatan Inazuma di 2023, 30% di antaranya dialokasikan untuk tabungan.*
        
        **d. ICOR 2023:**
        $$ICOR = \\frac{I_t}{\\Delta Y} = \\frac{PMTB_{2023}}{PDRB_{2023} - PDRB_{2022}} = \\frac{136}{120} = 1,133$$
        *Artinya, dibutuhkan tambahan investasi sebesar 1,133 miliar untuk menghasilkan tambahan output sebesar 1 miliar.*
        """)

with tab_24:
    st.header("Pembahasan Lengkap & Visual - UAS SNN 24/25")
    st.caption("Program Diploma IV STIS - T.A. 2024/2025")

    # SOAL 1
    with st.expander("Soal 1: PDB Pendekatan Produksi", expanded=True):
        st.markdown("""
        <div class="question-box">
            <strong>PERTANYAAN:</strong><br>
            Berikut ini adalah data Nilai Tambah Bruto (NTB) Atas Dasar Harga Berlaku (Miliar Rupiah) menurut lapangan usaha di Indonesia tahun 2024:<br>
            A. Pertanian, Kehutanan, dan Perikanan: 2.791.428 | B. Pertambangan: 2.026.589,2 | C. Industri Pengolahan: 4.202.866,9 | D. Pengadaan Listrik: 227.527,4 | E. Pengadaan Air: 14.258,8 | F. Konstruksi: 2.233.463,1 | G. Perdagangan: 2.892.694,6 | H. Transportasi: 1.358.116,6 | I. Akomodasi: 584.447,1 | J. Infokom: 960.021,6 | K. Jasa Keuangan: 922.810,9 | L. Real Estate: 520.728,1 | M,N. Jasa Perusahaan: 424.169,8 | O. Adm Pemerintahan: 673.717,5 | P. Jasa Pendidikan: 621.417,4 | Q. Jasa Kesehatan: 278.216,1 | R,S,T,U. Jasa Lainnya: 454.309,2.<br><br>
            <strong>a.</strong> Berdasarkan data di atas, hitunglah Nilai Tambah Bruto (NTB) seluruh lapangan usaha.<br>
            <strong>b.</strong> Jika Pajak Dikurang Subsidi Atas Produk adalah 952.181,7 (Miliar Rupiah), hitunglah Produk Domestik Bruto (PDB) tersebut.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="explanation">
            <strong>Konsep PDB Produksi:</strong> PDB adalah penjumlahan total dari Nilai Tambah Bruto (NTB) yang diciptakan oleh seluruh sektor (lapangan usaha) dalam suatu negara, ditambah dengan penyesuaian pajak neto atas produk. NTB sendiri didapatkan dari total nilai produksi (Output) dikurangi biaya bahan baku/penolong (Konsumsi Antara).
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**a. Hitunglah Nilai Tambah Bruto (NTB) seluruh lapangan usaha.**")
        st.markdown("Sesuai data, kita jumlahkan seluruh NTB dari lapangan usaha A hingga U:")
        
        data_ntb = {
            "Lapangan Usaha": ["Pertanian", "Pertambangan", "Industri", "Pengadaan Listrik", "Pengadaan Air", "Konstruksi", "Perdagangan", "Transportasi", "Akomodasi", "Informasi", "Jasa Keuangan", "Real Estate", "Jasa Perusahaan", "Administrasi Pemerintahan", "Jasa Pendidikan", "Jasa Kesehatan", "Jasa Lainnya"],
            "NTB (Miliar Rp)": [2791428.0, 2026589.2, 4202866.9, 227527.4, 14258.8, 2233463.1, 2892694.6, 1358116.6, 584447.1, 960021.6, 922810.9, 520728.1, 424169.8, 673717.5, 621417.4, 278216.1, 454309.2]
        }
        df_ntb = pd.DataFrame(data_ntb)
        
        total_ntb = df_ntb["NTB (Miliar Rp)"].sum()
        pajak_neto = 952181.7
        pdb = total_ntb + pajak_neto
        
        col1, col2 = st.columns(2)
        col1.metric("Total NTB Sektoral", f"Rp {total_ntb:,.1f} M")
        
        st.markdown("**b. Hitung Produk Domestik Bruto (PDB).**")
        st.markdown("Karena total NTB dihitung atas dasar Harga Dasar (Basic Price), untuk menjadikannya PDB berskala harga pasar, kita menambahkan komponen Pajak Atas Produk dikurangi Subsidi.")
        col2.metric("Total PDB (Harga Pasar)", f"Rp {pdb:,.1f} M")
        
        st.dataframe(df_ntb.style.format({"NTB (Miliar Rp)": "{:,.1f}"}), use_container_width=True)

    # SOAL 2
    with st.expander("Soal 2: PDB Pendekatan Pengeluaran"):
        st.markdown("""
        <div class="question-box">
            <strong>PERTANYAAN:</strong><br>
            a. Apa nama klasifikasi internasional yang digunakan untuk mengklasifikasikan komoditas yang dikonsumsi oleh rumah tangga? (nilai 5)<br>
            b. Sumber data yang digunakan untuk menyusun pengeluaran konsumsi rumah tangga adalah? (nilai 5)<br>
            c. Pengeluaran konsumsi akhir rumah tangga yang mencakup pemberian barang dan jasa dari pemerintah dan LNPRT disebut? (nilai 5)<br>
            d. Apakah PDB mencakup financial asset (saham, obligasi, dsb)? Jelaskan. (nilai 5)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        * **a. Klasifikasi internasional komoditas konsumsi:** 
          **COICOP** (Classification of Individual Consumption According to Purpose). Ini adalah standar dunia agar konsumsi pangan, pakaian, hingga perumahan bisa dibandingkan secara *apples-to-apples* antar negara.
          
        * **b. Sumber data utama konsumsi RT:** 
          **Susenas** (Survei Sosial Ekonomi Nasional) Modul Konsumsi yang diselenggarakan oleh BPS secara rutin untuk menangkap profil pengeluaran nyata rumah tangga.
          
        * **c. Pengeluaran RT ditambah natura pemerintah/LNPRT:** 
          **Konsumsi Akhir Aktual Rumah Tangga** (*Actual final consumption of households*). Karena masyarakat menikmati pendidikan dan kesehatan gratis dari pemerintah, hal ini dihitung sebagai konsumsi yang "aktual" dinikmati rumah tangga.
          
        * **d. Apakah Financial Asset (Saham/Obligasi) masuk PDB?**
          **Tidak.** PDB hanya mengukur penciptaan **barang dan jasa riil yang baru**. Transaksi saham dan obligasi hanyalah secarik kertas/data digital yang memindahkan klaim kekayaan (*transfer of wealth*) dari satu pihak ke pihak lain, tanpa ada pabrik atau output baru yang tercipta. Yang masuk ke PDB hanyalah "uang jasa/komisi" (fee/brokerage) dari pialang saham karena itu adalah aktivitas jasa riil.
        """)

    # SOAL 3
    with st.expander("Soal 3: Metode Revaluasi vs Deflasi"):
        st.markdown("""
        <div class="question-box">
            <strong>PERTANYAAN:</strong><br>
            Diketahui data Negara A adalah sebagai berikut dengan rasio konsumsi antara 50% dari nilai output. Hitunglah PDB Negara A pada tahun 2020-2025 atas dasar harga konstan tahun 2020 dengan menggunakan metode revaluasi dan deflasi. (nilai 20)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="explanation">
            <strong>Mengapa Harga Konstan?</strong> PDB Harga Berlaku akan membesar hanya karena barang menjadi lebih mahal (inflasi). Untuk melihat <strong>pertumbuhan riil fisik</strong>, kita harus mengunci harganya (Harga Konstan). Di bawah ini kita membandingkan dua metode pendekatan sesuai materi kelas.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 1. Alur Perbandingan Keseluruhan")
        st.markdown("""
```mermaid
flowchart TD
    A["Hitung PDB Konstan"] --> B["Metode Revaluasi"]
    A --> C["Metode Deflasi"]
    
    B --> B1["Output Konstan = Qt × Harga Tahun Dasar"]
    B --> B2["IC Konstan = Rasio Tetap 50% dari Output Konstan"]
    B1 --> B3["NTB Konstan = Output - IC"]
    B2 --> B3

    C --> C1["Output Konstan = Output Berlaku / Indeks Harga Output"]
    C --> C2["IC Konstan = Rasio Tetap 50% dari Output Konstan"]
    C1 --> C3["NTB Konstan = Output - IC"]
    C2 --> C3
    
    style B fill:#e0f2fe,stroke:#0369a1
    style C fill:#e0f2fe,stroke:#0369a1
```
        """)
        
        st.markdown("### 2. Cara Eksekusi Angka Tahun 2021 (Sebagai Contoh)")
        col_rev, col_def = st.columns(2)
        with col_rev:
            st.markdown("**Metode Revaluasi**")
            st.markdown("""
```mermaid
flowchart TD
    Q["Kuantitas 2021 = 426"] -->|"Dikali Harga Dasar P=4"| Out["Output Konstan = 1.704"]
    Out -->|"Asumsi Rasio Tetap 50%"| IC["Konsumsi Antara = 852"]
    Out -->|"Dikurang Konsumsi Antara"| PDB["PDB Konstan Revaluasi = 1.704 - 852 = 852"]
    IC -->|"Pengurang"| PDB
```
            """)
        with col_def:
            st.markdown("**Metode Deflasi**")
            st.markdown("""
```mermaid
flowchart TD
    OutB["Output Berlaku = 1.917"] -->|"Dibagi Indeks 1,125"| OutK["Output Konstan = 1.704"]
    OutK -->|"Asumsi Rasio Tetap 50%"| ICK["Konsumsi Antara = 852"]
    OutK -->|"Dikurang Konsumsi Antara"| PDB["PDB Konstan Deflasi = 1.704 - 852 = 852"]
    ICK -->|"Pengurang"| PDB
```
            """)

        tahun = [2020, 2021, 2022, 2023, 2024, 2025]
        qt = [400, 426, 450, 470, 480, 500]
        pt = [4, 4.5, 5, 5.3, 5.7, 6]
        
        # Kalkulasi Revaluasi
        out_rev = [q * 4 for q in qt]
        ic_rev = [0.5 * o for o in out_rev]
        pdb_rev = [o - i for o, i in zip(out_rev, ic_rev)]
        
        # Kalkulasi Deflasi (Tunggal)
        out_adhb = [q * p for q, p in zip(qt, pt)]
        ih_out = [(p / 4) * 100 for p in pt]
        
        out_def = [o / (idx / 100) for o, idx in zip(out_adhb, ih_out)]
        ic_def = [0.5 * o for o in out_def]
        pdb_def = [o - i for o, i in zip(out_def, ic_def)]
        
        df_soal3 = pd.DataFrame({
            "Tahun": tahun,
            "PDB (Revaluasi)": pdb_rev,
            "PDB (Deflasi)": pdb_def
        })
        
        st.dataframe(df_soal3.style.format({"PDB (Revaluasi)": "{:.2f}", "PDB (Deflasi)": "{:.2f}"}), use_container_width=True)
        
        st.warning("**Kesimpulan Perbandingan:** Karena metode Deflasi (tunggal) tetap menggunakan asumsi rasio biaya bahan baku (Konsumsi Antara) yang konstan dari Output Konstan, maka hasil akhirnya secara matematis terbukti **sama persis** dengan metode Revaluasi. Berbeda halnya jika menggunakan metode *Double Deflasi*.")

    # SOAL 4
    with st.expander("Soal 4: Analisis PDB (Pertumbuhan, Kontribusi, Inflasi)"):
        st.markdown("""
        <div class="question-box">
            <strong>PERTANYAAN:</strong><br>
            Berdasarkan data Negara B di tabel di bawah ini (PDB ADH Konstan 2023: 177, 2024: 188. PDB ADH Berlaku 2023: 190, 2024: 207):<br>
            a. Hitunglah laju pertumbuhan ekonomi dari 2023 ke 2024 dan interpretasikan hasilnya. (nilai 5)<br>
            b. Hitunglah sumber pertumbuhan ekonomi di setiap sektor pada tahun 2024 dan carilah sektor mana yang memberikan kontribusi terbesar terhadap pertumbuhan ekonomi di Negara B. (nilai 10)<br>
            c. Hitunglah laju indeks implisit di tahun 2024 dan interpretasikan hasilnya. (nilai 5)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="explanation">
            <strong>Analisis Makroekonomi PDB:</strong>
            <ul>
                <li><strong>Laju Pertumbuhan Ekonomi:</strong> Diukur menggunakan PDB Konstan karena ini secara murni mencerminkan tambahan fisik kuantitas barang/jasa, mengeliminasi ilusi lonjakan harga.</li>
                <li><strong>Source of Growth (SOG):</strong> Menjawab "Berapa persen sumbangsih suatu sektor dalam mengangkat <em>total</em> perekonomian?". Rumusnya adalah membagi selisih/tambahan PDB sektor tertentu dengan <em>Total</em> PDB tahun sebelumnya.</li>
                <li><strong>Indeks Implisit (PDB Deflator):</strong> Rasio antara PDB Berlaku dan PDB Konstan. Berfungsi sebagai pengukur tingkat inflasi untuk seluruh aktivitas perekonomian.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**4a. Laju Pertumbuhan 2024**")
            st.markdown("""
```mermaid
flowchart TD
    A["PDB Konstan 2023 = 177"] --> C{"Menghitung Selisih"}
    B["PDB Konstan 2024 = 188"] --> C
    C --> D["188 - 177 = 11"]
    D --> E["Laju = 11 / 177 = 6,21%"]
```
            """)
            g = (188 - 177) / 177 * 100
            st.metric("Pertumbuhan Fisik Ekonomi", f"{g:.2f}%")
            
        with col2:
            st.markdown("**4b. SOG (Sektor Sekunder)**")
            st.markdown("""
```mermaid
flowchart TD
    A["Sekunder 2024 = 75"] --> C["Selisih Tambahan = 5"]
    B["Sekunder 2023 = 70"] --> C
    C --> D["Dibagi Total PDB 2023 (177)"]
    D --> E["Kontribusi Sektor = 2,82%"]
```
            """)
            sog_sekunder = (75-70)/177*100
            st.metric("Kontribusi Sektor Sekunder", f"{sog_sekunder:.2f}%")
            
        with col3:
            st.markdown("**4c. Laju Indeks Implisit**")
            st.markdown("""
```mermaid
flowchart TD
    A["PDB Berlaku 2023"] -->|"190 / 177"| C1["Indeks 2023 = 107,34"]
    B["PDB Berlaku 2024"] -->|"207 / 188"| C2["Indeks 2024 = 110,11"]
    C1 -->|"Penyebut"| Laju["Laju Inflasi = 2,57%"]
    C2 -->|"Pembilang"| Laju
```
            """)
            idx_2023 = (190 / 177) * 100
            idx_2024 = (207 / 188) * 100
            laju_implisit = (idx_2024 - idx_2023) / idx_2023 * 100
            st.metric("Inflasi PDB Makro", f"{laju_implisit:.2f}%")
            
        st.markdown("**Interpretasi Analisis Makro 2024:**")
        st.markdown("Perekonomian secara volume fisik tumbuh 6,21%, ditopang paling besar secara seimbang oleh Sektor Sekunder dan Tersier (masing-masing menyumbang porsi 2,82%). Tingkat inflasi seluruh kegiatan ekonomi (Indeks Implisit) tercatat 2,57%.")

    # SOAL 5
    with st.expander("Soal 5: Makroekonomi (ICOR & Elastisitas Tenaga Kerja)"):
        st.markdown("""
        <div class="question-box">
            <strong>PERTANYAAN:</strong><br>
            1. Jika PDB tahun 2023 sebanyak 10.000 trilyun, dan pertumbuhan ekonomi tahun 2025 ditargetkan 6 persen. Berapa tambahan investasi yang diperlukan pemerintah jika diketahui ICOR nya 0.17 (nilai 5)<br>
            2. Berikut adalah data PDB dan Tenaga Kerja di suatu wilayah ekonomi...<br>
            a. Hitung pertumbuhan PDB, Tenaga kerja dan elastisitas tenaga kerja periode 2021-2022 dan periode 2023-2022 (nilai 10)<br>
            b. Apakah pertumbuhan ekonomi 2023 lebih padat karya dibanding 2022? Jelaskan dengan hasil dari no 1. (nilai 5)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="explanation">
            <strong>1. ICOR (Incremental Capital Output Ratio):</strong> Angka ini membongkar seberapa efisien investasi (modal) sebuah negara. Angka ICOR sebesar 0,17 adalah sangat luar biasa efisien; yang berarti untuk menghasilkan 1 unit output (Rp1 Triliun), hanya butuh suntikan modal sebesar 0,17 unit (Rp170 Miliar).<br><br>
            <strong>2. Elastisitas Tenaga Kerja:</strong> Indikator ini menjabarkan kemampuan ekonomi mencetak lahan pekerjaan, menjawab pertanyaan: "Untuk setiap 1% pertumbuhan ekonomi, berapa persen lonjakan jumlah lapangan kerja yang terbuka?".
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 1. Kebutuhan Tambahan Investasi (ICOR)")
        
        colA, colB = st.columns([1.5, 1])
        with colA:
            st.markdown("""
```mermaid
flowchart LR
    A["Target Pertumbuhan (6%)"] --> B["Hitung Tambahan Output ΔY"]
    C["PDB Awal 10.000"] --> B
    B -->|"ΔY = 600"| D["Kebutuhan Investasi (ΔK)"]
    E["ICOR 0,17"] --> D
    D --> F["Investasi = 600 × 0,17 = 102 Triliun"]
```
            """)
        with colB:
            dY = 0.06 * 10000
            invest = 0.17 * dY
            st.metric("Tambahan Output (ΔY)", f"Rp {dY:,.0f} T")
            st.metric("Investasi Dibutuhkan", f"Rp {invest:,.0f} T")
        
        st.markdown("---")
        st.markdown("### 2. Elastisitas Tenaga Kerja")
        
        colC, colD = st.columns([1.5, 1])
        with colC:
            st.markdown("""
```mermaid
flowchart TD
    F["% Penambahan Tenaga Kerja"] --> H{"Dibagi"}
    G["% Pertumbuhan PDB Riil"] --> H
    H --> I["Angka Elastisitas TK"]
```
            """)
        with colD:
            elastisitas_2022 = ((133.56 - 131.05) / 131.05) / ((10.63 - 10.23) / 10.23)
            elastisitas_2023 = ((136.46 - 133.56) / 133.56) / ((11.498 - 10.63) / 10.63)
            st.metric("Elastisitas TK (2021-2022)", f"{elastisitas_2022:.2f}")
            st.metric("Elastisitas TK (2022-2023)", f"{elastisitas_2023:.2f}")
        
        st.warning("**Kesimpulan (Soal 5.2b):** Tahun 2023 **TIDAK** lebih padat karya dibandingkan 2022. Fakta bahwa angka elastisitas menurun tajam (dari 0,49 ke 0,27) menjadi bukti bahwa pertumbuhan PDB yang sangat ngebut di tahun 2023 (mencapai 8,17%) lebih banyak ditopang oleh padat modal (*capital-intensive*) alias mesin-mesin, serta peningkatan produktivitas yang eksponensial; **bukan** ditopang oleh masifnya penyerapan sumber daya manusia baru. Karena itu, tahun 2022 adalah tahun yang jauh lebih inklusif dan padat karya (*labor-intensive*).")
