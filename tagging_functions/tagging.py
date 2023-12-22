from pydantic import BaseModel, Field

class Tagging(BaseModel):
    """Tag the piece of text with particular info."""
    city_to: str = Field(description="город, куда хочет поехать пользователь, например Казань")
    city_from: str = Field(description="город, откуда пользователь хочет поехать, например, Москва")
    day: str = Field(description="день, когда пользователь хочет, если сегодня, то выведи 0, если завтра то 1, и так по +1 за каждый день, если дата, то выведи в формате ДД.ММ")
    start_time: str = Field(description="начало промежутка времени, когда пользователь хочет отправиться, например 18:00")
    end_time: str = Field(description="конец промежутка времени, когда пользователь хочет отпрравиться, например 20:00")
    price: str = Field(description="ограничение по цене, например если говорит до 5 тысяч, то пиши 5000")
