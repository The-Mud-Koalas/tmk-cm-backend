from communalspace.exceptions import InvalidRequestException
from communalspace.settings import POINTS_PER_ATTENDANCE
from event.exceptions import InvalidCheckInCheckOutException


def validate_event_is_on_going(event):
    if not event.is_ongoing():
        raise InvalidRequestException('Event has not started or has been completed')


def validate_user_is_inside_event_location(event, user_latitude, user_longitude):
    if not event.check_user_is_inside_event(user_latitude, user_longitude):
        raise InvalidRequestException(f'User is currently not inside event location')


def validate_user_can_check_in(user, participation):
    if user.is_currently_attending_event() or participation.get_is_currently_attending():
        raise InvalidCheckInCheckOutException('User is currently attending an event')


def check_in_user(user, attendable_event, participation):
    check_in_data = participation.check_in()
    user.set_currently_attended_event(attendable_event)
    user.set_currently_attending_role(participation.get_participation_type())
    return check_in_data


def validate_user_can_check_out(participation):
    if not participation.get_is_currently_attending():
        raise InvalidCheckInCheckOutException('User is currently not attending event')


def handle_check_out_reward_grant(user, check_out_data, attendable_participation):
    reward_and_check_out_data = {**check_out_data}
    if attendable_participation.is_eligible_for_reward() and not attendable_participation.has_been_rewarded():
        user.add_reward(POINTS_PER_ATTENDANCE)
        attendable_participation.set_rewarded(True)
        reward_and_check_out_data['is_rewarded'] = True

    else:
        reward_and_check_out_data['is_rewarded'] = False

    return reward_and_check_out_data


def self_check_out_user(user, attendable_participation, user_latitude, user_longitude):
    check_out_data = attendable_participation.self_check_out(user_latitude, user_longitude)
    user.remove_currently_attended_event()
    return handle_check_out_reward_grant(user, check_out_data, attendable_participation)