import pxz


def add_material(mat_name):  # add a new material to the Pixyz material library
    new_mat = pxz.material.createMaterial(mat_name, "PBR")  # create a new PBR material

    # TODO: skip if material already exists

    # Material structure:
    # albedo
    # metallic
    # roughness
    # opacity
    # normal
    # ao

    # Set the material properties based on the material name
    if "Metal" or "Metall" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 1.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.1)
    elif "Glass" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.0)
        pxz.core.setProperty(new_mat, 'opacity', 0.25)
    elif "Plastic" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.5)
    elif "Rubber" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 1.0)
    elif "Concrete" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.5)
    elif "Wood" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.5)
        pxz.core.setProperty(new_mat, 'albedo', str([0.75, 0.5, 0.25]))
    elif "PowderCoating" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.5)
    elif "ConveyorBelt" in mat_name:
        pxz.core.setProperty(new_mat, 'metallic', 0.0)
        pxz.core.setProperty(new_mat, 'roughness', 0.5)
    else:
        pass

    # Set the material composition based on the material name
    if "Dull" in mat_name:
        pxz.core.setProperty(new_mat, 'roughness', 1.0)
    elif "Glossy" in mat_name:
        pxz.core.setProperty(new_mat, 'roughness', 0.0)
    elif "LightlyBrushed" in mat_name:
        pxz.core.setProperty(new_mat, 'roughness', 0.5)
        pxz.core.setProperty(new_mat, 'metallic', 0.75)
        pxz.core.setProperty(new_mat, 'albedo', str([0.75, 0.75, 0.75]))
    elif "StronglyBrushed" in mat_name:
        pxz.core.setProperty(new_mat, 'roughness', 0.25)
        pxz.core.setProperty(new_mat, 'metallic', 0.75)
        pxz.core.setProperty(new_mat, 'albedo', str([0.25, 0.25, 0.25]))
    else:
        pass

    # Set the material color based on the material name
    if "Red" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([1.0, 0.0, 0.0]))
    elif "Green" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.0, 1.0, 0.0]))
    elif "Blue" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.0, 0.0, 1.0]))
    elif "Yellow" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([1.0, 1.0, 0.0]))
    elif "Cyan" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.0, 1.0, 1.0]))
    elif "Orange" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([1.0, 0.5, 0.0]))
    elif "White" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([1.0, 1.0, 1.0]))
    elif "Black" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.0, 0.0, 0.0]))
    elif "Gray" or "Grey" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.5, 0.5, 0.5]))
    elif "LightGray" or "LightGrey" or "Light" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.75, 0.75, 0.75]))
    elif "DarkGray" or "DarkGrey" or "Dark" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.25, 0.25, 0.25]))
    elif "Ocker" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.75, 0.5, 0.25]))
    elif "Beige" in mat_name:
        pxz.core.setProperty(new_mat, 'albedo', str([0.75, 0.75, 0.5]))
    else:
        pass
