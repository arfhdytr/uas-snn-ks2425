import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Pembahasan UAS SNN", 
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
</style>
""", unsafe_allow_html=True)

st.title("Pembahasan Lengkap & Visual - UAS Statistik Neraca Nasional")
st.caption("Program Diploma IV STIS - T.A. 2024/2025")

# SOAL 1
with st.expander("Soal 1: PDB Pendekatan Produksi", expanded=True):
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
with st.expander("Soal 3: Metode Revaluasi vs Deflasi Ganda"):
    st.markdown("""
    <div class="explanation">
        <strong>Mengapa Harga Konstan?</strong> PDB Harga Berlaku akan membesar hanya karena barang menjadi lebih mahal (inflasi). Untuk melihat <strong>pertumbuhan riil fisik</strong>, kita harus mengunci harganya (Harga Konstan). Di bawah ini kita membandingkan dua metode pendekatan.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 1. Alur Perbandingan Keseluruhan")
    st.markdown("""
```mermaid
flowchart TD
    A["Hitung PDB Konstan"] --> B["Metode Revaluasi"]
    A --> C["Metode Deflasi Ganda"]
    
    B --> B1["Output Konstan = Qt × Harga Tahun Dasar"]
    B --> B2["IC Konstan = Rasio Tetap 50% dari Output Konstan"]
    B1 --> B3["NTB Konstan = Output - IC"]
    B2 --> B3

    C --> C1["Output Konstan = Output Berlaku / Indeks Harga Output"]
    C --> C2["IC Konstan = IC Berlaku / Indeks Harga IC"]
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
        st.markdown("**Metode Deflasi Ganda**")
        st.markdown("""
```mermaid
flowchart TD
    OutB["Output Berlaku = 1.917"] -->|"Dibagi Indeks 1,125"| OutK["Output Konstan = 1.704"]
    ICB["IC Berlaku = 958,5"] -->|"Dibagi Indeks 1,05"| ICK["Konsumsi Antara = 912,86"]
    OutK -->|"Dikurang Konsumsi Antara"| PDB["PDB Konstan Deflasi = 1.704 - 912,86 = 791,14"]
    ICK -->|"Pengurang"| PDB
```
        """)

    tahun = [2020, 2021, 2022, 2023, 2024, 2025]
    qt = [400, 426, 450, 470, 480, 500]
    pt = [4, 4.5, 5, 5.3, 5.7, 6]
    ihka = [100, 105, 107, 110, 113, 115]
    
    out_rev = [q * 4 for q in qt]
    ic_rev = [0.5 * o for o in out_rev]
    pdb_rev = [o - i for o, i in zip(out_rev, ic_rev)]
    
    out_adhb = [q * p for q, p in zip(qt, pt)]
    ic_adhb = [0.5 * o for o in out_adhb]
    ih_out = [(p / 4) * 100 for p in pt]
    
    out_def = [o / (idx / 100) for o, idx in zip(out_adhb, ih_out)]
    ic_def = [i / (idx / 100) for i, idx in zip(ic_adhb, ihka)]
    pdb_def = [o - i for o, i in zip(out_def, ic_def)]
    
    df_soal3 = pd.DataFrame({
        "Tahun": tahun,
        "PDB (Revaluasi)": pdb_rev,
        "PDB (Deflasi Ganda)": pdb_def
    })
    
    st.dataframe(df_soal3.style.format({"PDB (Revaluasi)": "{:.2f}", "PDB (Deflasi Ganda)": "{:.2f}"}), use_container_width=True)
    
    st.warning("**Kesimpulan Perbandingan:** Pada metode deflasi ganda, Indeks Harga Konsumsi Antara (IHKa) naik secara lebih lambat (sebesar 15% dari 100 ke 115) bila dibandingkan dengan kenaikan harga Output (yang melonjak tajam 50% dari 4 ke 6). Dampaknya, persentase struktur biaya riil bahan baku akan tampak membengkak, sehingga menghimpit margin nilai tambah. Hal inilah yang menyebabkan pencatatan nilai PDB Riil secara deflasi menurun perlahan.")

# SOAL 4
with st.expander("Soal 4: Analisis PDB (Pertumbuhan, Kontribusi, Inflasi)"):
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
    
    st.info("Catatan Data: \nPDB Konstan 2023 = 177 | PDB Konstan 2024 = 188. \nPDB Berlaku 2023 = 190 | PDB Berlaku 2024 = 207.")
    
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

# SOAL 5
with st.expander("Soal 5: Makroekonomi (ICOR & Elastisitas Tenaga Kerja)"):
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
