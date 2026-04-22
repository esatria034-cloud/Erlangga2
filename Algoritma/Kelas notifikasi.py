import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class EmailNotifikasi:
    def __init__(self, pesan, alamat_email_tujuan, file_path):
        self.pesan = pesan
        self.alamat_email_tujuan = alamat_email_tujuan
        self.file_path = file_path

    def kirim_notifikasi(self):
        try:
            pengirim = "esatria034@gmail.com"
            password = "fdxyizcgrbdnbtiv"  # ganti ini

            # bikin email
            msg = MIMEMultipart()
            msg['Subject'] = "Kirim File dari Python"
            msg['From'] = pengirim
            msg['To'] = self.alamat_email_tujuan

            # isi pesan
            msg.attach(MIMEText(self.pesan))

            # attach file
            with open(self.file_path, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=self.file_path
                )
                msg.attach(attachment)

            # kirim email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(pengirim, password)
            server.send_message(msg)
            server.quit()

            print("✅ Email dan file berhasil dikirim!")

        except Exception as e:
            print("❌ Gagal:", e)


notif = EmailNotifikasi(
    "Ini email dari braderr Satria Erlangga, dari kelas 03TPLP002 berhasil terkirim + file",
    "esatria034@gmail.com",
    "kelas notifikasi.py"   # ⬅️ ganti sesuai file kamu
)

notif.kirim_notifikasi()