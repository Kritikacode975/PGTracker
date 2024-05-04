def handle_uploaded_file(f):
    with open("pgfinder_admin/static/images/" + f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
