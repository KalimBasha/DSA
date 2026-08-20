'''
Builder solves how to construct a complex object step by step.

Build a Hotstar subscription plan builder:
Mandatory:
user_name
plan_type ("Mobile", "Super", "Premium")

Optional:
is_annual (bool, default False)
add_sports_pack (bool, default False)
add_kids_pack (bool, default False)
max_screens (int, default 1)
download_limit (int, default 25)

build() must validate mandatory fields and raise ValueError if missing.
Calling code — three users:

Basic mobile user — mandatory only
Family user — Premium, annual, 4 screens, kids pack
Sports fan — Super, sports pack, 2 screens, 50 downloads

Trace:
python# TRACE: .with_sports_pack().with_max_screens(2).build() chained on builder
# After with_sports_pack() →
# After with_max_screens(2) →
# After build() →

'''


# base class for subscription created empty
class HotstarSubscription:
    def __init__(self):
        self.user_name = None
        self.plan_type = None
        self.is_annual = False
        self.add_sports_pack = False
        self.add_kids_pack = False
        self.max_screens = 1
        self.download_limit = 25

    def __str__(self):
        return (f"User: {self.user_name} | Plan: {self.plan_type} | "
                f"Annual: {self.is_annual} | Screens: {self.max_screens} | "
                f"Sports: {self.add_sports_pack} | Kids: {self.add_kids_pack} | "
                f"Downloads: {self.download_limit}")


class HotstarSubscriptionBuilder:
    def __init__(self, username: str, plan: str):
        self.__subscription = HotstarSubscription()
        self.__subscription.user_name = username
        self.__subscription.plan_type = plan

    def with_annual(self):
        self.__subscription.is_annual = True
        return self

    def with_sports_pack(self):
        self.__subscription.add_sports_pack = True
        return self

    def with_kids_pack(self):
        self.__subscription.add_kids_pack = True
        return self

    def with_max_screens(self, screens: int):
        self.__subscription.max_screens = screens
        return self

    def with_download_limit(self, limit: int):
        self.__subscription.download_limit = limit
        return self

    def build(self) -> HotstarSubscription:
        if not self.__subscription.user_name:
            raise ValueError("Username is mandatory")
        if not self.__subscription.plan_type:
            raise ValueError("Plan type is mandatory")
        return self.__subscription


# Calling code
basic_user = (
    HotstarSubscriptionBuilder("Kalim", "Mobile")
    .build()
)
print(basic_user)

premium_user = (
    HotstarSubscriptionBuilder("Kalim", "Premium")
    .with_annual()
    .with_kids_pack()
    .with_max_screens(4)
    .build()
)
print(premium_user)

super_user = (
    HotstarSubscriptionBuilder("Kalim", "Super")
    .with_sports_pack()
    .with_max_screens(2)
    .with_download_limit(50)
    .build()
)
print(super_user)

# TRACE: .with_sports_pack().with_max_screens(2).build() chained on builder
# After with_sports_pack() → sets add_sports_pack=True on subscription, returns self (builder)
# After with_max_screens(2) → sets max_screens=2 on subscription, returns self (builder)
# After build() → validates user_name and plan_type exist, returns finished HotstarSubscription object

# Trace 
# whenever an instance is created for builder first step we are initializing or calling this builder with our needs
# for example will see for premium users
# first calling the builder with mandatory fields like name and plan type
# then add optional fields but needed for premium plan like annual package with 4 screens and kids pack
# later that build will initialize the actual HotspotSubscription class with the values and returning the response