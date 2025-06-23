from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User

from datetime import date

app = create_app()

with app.app_context():
    print(" Seeding data...")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    user = User(username="admin")
    user.set_password("password123")
    db.session.add(user)


    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Zendaya", occupation="Actor")
    guest3 = Guest(name="Serena Williams", occupation="Tennis Player")
    db.session.add_all([guest1, guest2, guest3])

    ep1 = Episode(date=date(2024, 10, 1), number=101)
    ep2 = Episode(date=date(2024, 10, 2), number=102)
    db.session.add_all([ep1, ep2])

    ap1 = Appearance(rating=5, guest=guest1, episode=ep1)
    ap2 = Appearance(rating=4, guest=guest2, episode=ep1)
    ap3 = Appearance(rating=5, guest=guest3, episode=ep2)
    db.session.add_all([ap1, ap2, ap3])

    db.session.commit()
    print(" Done seeding!")
