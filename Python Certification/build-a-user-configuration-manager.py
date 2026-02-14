# Create a dictionary named test_settings
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

# Function to add a setting
def add_setting(settings_dict, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

# Function to update a setting
def update_setting(settings_dict, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Function to delete a setting
def delete_setting(settings_dict, key):
    key = key.lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

# Function to view settings
def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings_dict.items():
        result += f"{key.capitalize()}: {value}\n"
    return result
