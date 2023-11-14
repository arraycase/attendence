import boto3

# function to compare the faces of people present in 2 images
def compare_faces(sourceFile, targetFile):

    # need to generate a profile-name for this to run (an aws account is needed)
    session = boto3.Session(profile_name='profile-name')

    client = session.client('rekognition')
    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')
    response = client.compare_faces(SimilarityThreshold=80,
    SourceImage={'Bytes': imageSource.read()},
    TargetImage={'Bytes': imageTarget.read()})
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
        str(position['Left']) + ' ' +
        str(position['Top']) +
        ' matches with ' + similarity + '% confidence')
    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])

def main():
    source_file = '1.jpg'
    target_file = '2.jpg'
    face_matches = compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))

if __name__ == "__main__":
    main()
