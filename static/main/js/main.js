let TOKEN = '7362615665:AAEZRbtp_3tqhtRlzPub4Wvt1ZwkBMigK4U';
let CHAT_ID = -1002496843835;
let URL_API = `https://api.telegram.org/bot${TOKEN}/sendMessage`;

document.getElementById('tg').addEventListener('submit', function (e) {
  e.preventDefault();

  const form = this;
  const name = form.name.value.trim();
  const number = form.number.value.trim();

  if (!name || !number) {
    alert("Iltimos, barcha maydonlarni to'ldiring!");
    return;
  }

  let message = `<b>Ro'yxat</b>\n`;
  message += `<b>Ism:</b> ${name}\n`;
  message += `<b>Raqam:</b> +${number}\n`;

  console.log(message);

  axios
    .post(URL_API, {
      chat_id: CHAT_ID,
      parse_mode: 'html',
      text: message,
    })
    .then(() => {
      form.name.value = '';
      form.number.value = '';

      alert("Ma'lumot muvaffaqiyatli yuborildi!");
    })
    .catch((err) => {
      console.warn(err);

      alert("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.");
    })
    .finally(() => {
      console.log('Tugadi');
    });
});



function scrollToSection(id) {
  const element = document.getElementById(id);
  if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });

  } else {
      console.warn(`Section with id ${id} not found`);
  }
}


