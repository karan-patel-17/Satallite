initial_state = {
    'orientation': 'North',
    'solar_panels': 'Inactive',
    'data_collected': 0,
}

def satellite_state():
    state_str = f"*******\nSatellite State:\nOrientation: {initial_state['orientation']}\nSolar Panels: {initial_state['solar_panels']}\nData Collected: {initial_state['data_collected']}\n*********"
    print(state_str)

def execute_command(command, direction=None):
    if command == 'rotate':
        if direction in ('North', 'South', 'East', 'West'):
            initial_state['orientation'] = direction
    elif command == 'activate_panels':
        initial_state['solar_panels'] = 'Active'
    elif command == 'deactivate_panels':
        initial_state['solar_panels'] = 'Inactive'
    elif command == 'collect_data':
        if initial_state['solar_panels'] == 'Active':
            initial_state['data_collected'] += 10

    satellite_state()

if __name__ == '__main__':
    print("Satellite Command System")
    satellite_state()

    while True:
        command = input("From the Command Given Below: \nrotate\nactivate_panels\ndeactivate_panels\ncollect_data\nexit\nEnter the Command:")
        if command == 'exit':
            break

        if command == 'rotate':
            direction = input("*******\nEnter direction from below option\nNorth\nSouth\nEast\nWest\n*********\n")
            execute_command(command, direction)
        else:
            execute_command(command)
