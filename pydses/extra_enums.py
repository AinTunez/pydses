"""
@author: grimrhapsody
"""


from enum import Enum


""" EVENT_DEFINE.LUA """


# Verbatim
LOCAL_PLAYER = 10000


# Verbatim
NET_PLAYER = 10001


class message_category(Enum):
    """
    Extended original abbreviated name ("MSG_CATEGORY").
    Obvious enough to assume "message" is the proper extended word.
    """
    sample = 0
    talk = 1
    blood = 2  # Likely refers to BloodMsg's, which are orange soapstone messages rather than bloodstains IIRC
    item = 10
    weapon = 11
    protector = 12
    accessory = 13
    item_exp = 14
    weapon_exp = 15
    protector_exp = 16
    accessory_exp = 17
    event = 30
    dialog = 78


class info_menu_type(Enum):
    list = 0
    simple = 1


class event_hit_type(Enum):
    """
    Extended original abbreviated name ("EV_HIT") and made more specific.
    This is only an assumption of the full-length word.
    """
    chr = 1
    hit = 2
    all = 3


class net_attribute(Enum):
    """
    Note: Enum name changed from the default name of "ATTR", to make it more contextually specific,
          since it is a misc. value that is hardly used, if at all.
    """
    session = 1
    no_session = 2
    host = 4
    client = 8
    live = 16
    gray = 32  # Spelling changed from "GREY" so it matches other enums.
    white = 64
    black = 128
    all = 255


class talk_attribute(Enum):
    """
    Extended original abbreviated name ("TALK_ATTR"). This is only an assumption
    of the full-length word.
    """
    repeat = 1
    pad = 2
    draw = 4
    voice = 8
    all = 255


class player_death_type(Enum):
    """
    Renamed from original name "DEATH_STATE" to avoid confusion with EMELD's "Death State",
    which has the values "Alive" and "Dead"

    Values renamed to their ingame names for both easier understanding and shorter names.

    Original event_define.lua values:
    DEATH_STATE_Normal = 0
    DEATH_STATE_MagicResurrection = 1
    DEATH_STATE_RingNormalResurrection = 2
    DEATH_STATE_RingCurseResurrection = 3
    """
    normal = 0
    magic_revival = 1  # This is what the unused text banner texture says IIRC.
    ring_revival = 2
    rare_ring_revival = 3


class summon_param_type(Enum):
    none = 0
    white = -1
    black = -2
    force_join_black = -4  # Fixed typo in original ("FroceJoinBlack")
    detect_black = -4
    invade_nito = -7
    dragonewt = -10
    invade_bounty = -11
    coliseum = -12


""" This is probably completely useless, but feel free to uncomment if you find a use:
class soul_rate(Enum):
    small = 0.1
    medium = 0.5
    large = 0.5
"""


class invade_type(Enum):
    none = 0
    normal_white = 1
    normal_black = 2
    force_join_black = 3
    detect_black = 4
    white_rescue = 5
    black_rescue = 6
    nito = 7
    thieves_guild = 8
    otouto_umbasa = 9
    dragonewt = 10
    invade_bounty = 11
    coliseum_one_b = 12
    coliseum_two_a2 = 13
    coliseum_two_b1 = 14
    coliseum_two_b2 = 15
    coliseum_br_b = 16
    coliseum_br_c = 17
    coliseum_br_d = 18


