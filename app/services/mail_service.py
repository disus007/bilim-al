import aiosmtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings


def generate_code(length: int = 6) -> str:
    """Генерирует случайный 6-значный код."""
    return ''.join(random.choices(string.digits, k=length))


async def send_reset_email(to_email: str, code: str, username: str) -> bool:
    """
    Отправляет письмо с кодом восстановления пароля.
    Возвращает True если успешно, False если ошибка.
    """
    try:
        # Создаём письмо
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Bilim Al — Код восстановления пароля: {code}"
        msg["From"]    = settings.MAIL_FROM
        msg["To"]      = to_email

        # HTML версия письма
        html = f"""
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                    max-width: 480px; margin: 0 auto; padding: 40px 20px;">

            <div style="text-align:center; margin-bottom:32px">
                <div style="width:48px; height:48px; background:#2563eb; border-radius:12px;
                            display:inline-flex; align-items:center; justify-content:center;
                            font-size:24px; margin-bottom:16px">🎓</div>
                <h1 style="font-size:24px; font-weight:700; color:#0f172a; margin:0">
                    Bilim Al
                </h1>
            </div>

            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:16px;
                        padding:32px; margin-bottom:24px">
                <h2 style="font-size:18px; font-weight:600; color:#0f172a; margin:0 0 8px">
                    Восстановление пароля
                </h2>
                <p style="color:#64748b; font-size:14px; margin:0 0 24px; line-height:1.6">
                    Привет, <strong>{username}</strong>! Вы запросили восстановление пароля.
                    Используйте код ниже для входа:
                </p>

                <div style="background:#ffffff; border:2px solid #2563eb; border-radius:12px;
                            padding:20px; text-align:center; margin-bottom:24px">
                    <div style="font-size:36px; font-weight:800; letter-spacing:8px;
                                color:#2563eb; font-family:monospace">
                        {code}
                    </div>
                </div>

                <p style="color:#94a3b8; font-size:12px; margin:0; text-align:center">
                    Код действителен 15 минут. Если вы не запрашивали сброс пароля —
                    просто проигнорируйте это письмо.
                </p>
            </div>

            <p style="color:#cbd5e1; font-size:12px; text-align:center; margin:0">
                © 2025 Bilim Al — Интеллектуальная система обучения
            </p>
        </div>
        """

        msg.attach(MIMEText(html, "html"))

        # Отправляем через Gmail SMTP
        await aiosmtplib.send(
            msg,
            hostname=settings.MAIL_SERVER,
            port=settings.MAIL_PORT,
            username=settings.MAIL_USERNAME,
            password=settings.MAIL_PASSWORD,
            start_tls=True,
        )
        return True

    except Exception as e:
        print(f"[MAIL ERROR] {e}")
        return False


async def send_verification_email(to_email: str, code: str, username: str) -> bool:
    """Отправляет письмо с кодом подтверждения email при регистрации."""
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Bilim Al — Подтверждение email: {code}"
        msg["From"]    = settings.MAIL_FROM
        msg["To"]      = to_email

        html = f"""
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                    max-width: 480px; margin: 0 auto; padding: 40px 20px;">

            <div style="text-align:center; margin-bottom:32px">
                <div style="width:48px; height:48px; background:#2563eb; border-radius:12px;
                            display:inline-flex; align-items:center; justify-content:center;
                            font-size:24px; margin-bottom:16px">🎓</div>
                <h1 style="font-size:24px; font-weight:700; color:#0f172a; margin:0">
                    Bilim Al
                </h1>
            </div>

            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:16px;
                        padding:32px; margin-bottom:24px">
                <h2 style="font-size:18px; font-weight:600; color:#0f172a; margin:0 0 8px">
                    Подтверждение email
                </h2>
                <p style="color:#64748b; font-size:14px; margin:0 0 24px; line-height:1.6">
                    Привет, <strong>{username}</strong>! Добро пожаловать в Bilim Al.
                    Введите код ниже чтобы подтвердить ваш email:
                </p>

                <div style="background:#ffffff; border:2px solid #16a34a; border-radius:12px;
                            padding:20px; text-align:center; margin-bottom:24px">
                    <div style="font-size:36px; font-weight:800; letter-spacing:8px;
                                color:#16a34a; font-family:monospace">
                        {code}
                    </div>
                </div>

                <p style="color:#94a3b8; font-size:12px; margin:0; text-align:center">
                    Код действителен 15 минут.
                </p>
            </div>

            <p style="color:#cbd5e1; font-size:12px; text-align:center; margin:0">
                © 2025 Bilim Al — Интеллектуальная система обучения
            </p>
        </div>
        """

        msg.attach(MIMEText(html, "html"))

        await aiosmtplib.send(
            msg,
            hostname=settings.MAIL_SERVER,
            port=settings.MAIL_PORT,
            username=settings.MAIL_USERNAME,
            password=settings.MAIL_PASSWORD,
            start_tls=True,
        )
        return True

    except Exception as e:
        print(f"[MAIL ERROR] {e}")
        return False