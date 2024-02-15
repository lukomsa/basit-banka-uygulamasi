# basit-banka-uygulamasi

**basit-banka-uygulamasi**  adlı bu Python projesi, Tkinter kütüphanesini kullanarak basit bir banka uygulaması oluşturmaktadır. Kullanıcılar bu uygulama ile aşağıdaki işlemleri gerçekleştirebilirler:

* **Para Yatırma:** Kullanıcılar, bir metin kutusuna miktarı girerek para yatırabilirler. Para birimi otomatik olarak seçilir veya kullanıcı tarafından değiştirilebilir.
* **Para Çekme:** Kullanıcılar, bir metin kutusuna miktarı girerek para çekebilirler. Yetersiz bakiye durumunda, kullanıcıya bir uyarı mesajı gösterilir.
* **Bakiye Gösterme:** Kullanıcılar, "Bakiye Göster" butonuna tıklayarak güncel bakiyelerini görebilirler. Bakiye, seçilen para biriminde gösterilir.
* **Para Birimi Seçme:** Kullanıcılar, bir seçim listesinden para birimini seçebilirler. Seçilen para birimi, tüm işlemler için geçerli olacaktır.

**Uygulama:**

* **BankaHesabı** adında bir sınıf, bakiye, para birimi ve kur bilgileri gibi banka hesabına ait bilgileri saklar.
* **Tkinter** kütüphanesi, pencere, metin kutusu, buton ve seçim listesi gibi arayüz elemanlarını oluşturmak için kullanılır.
* **para_yatir**, **para_cek**, **bakiye_goster** ve **para_birimi_sec** fonksiyonları, para yatırma, para çekme, bakiye gösterme ve para birimi seçme işlemlerini gerçekleştirir.
* **onselect** fonksiyonu, seçim listesinin seçim değiştiğinde çalışır ve para birimini ve bakiye etiketini günceller.

**Bu kod, Python ve Tkinter kullanarak basit bir banka uygulaması oluşturmak isteyenler için faydalı bir kaynak olabilir.**

**Ek Özellikler:**

* Farklı hesap türleri (örneğin, tasarruf hesabı, cari hesap) eklenebilir.
* Hesap hareketlerinin gösterilmesi için bir tablo eklenebilir.
* Kullanıcı kimlik doğrulama ve şifreleme eklenebilir.

**Not:** Bu kod, eğitim amaçlıdır ve ticari kullanım için uygun değildir.
