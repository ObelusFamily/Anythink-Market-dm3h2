from typing import List, Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel


img_placeholder = "Anythink-Market-dm3h2/frontend/public/placeholder.png";

class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: img_placeholder
    body: Optional[str]
