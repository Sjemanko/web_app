# Person
### from lab4.models import Person
### from lab4.serializers import PersonSerializer
### person = Person.objects.get(id=1)
### person 
<Person: Mike Wazowski>
### serializer = PersonSerializer(person)
### serializer.data  
{'id': 1, 'first_name': 'Mike', 'last_name': 'Wazowski', 'month_birth': 6, 'team': 2, 'created_at': '2022-11-05T20:25:50.441553Z'}
### from rest_framework.renderers import JSONRenderer
### from rest_framework.parsers import JSONParser
### content = JSONRenderer().render(serializer.data)
### content
b'{"id":1,"first_name":"Mike","last_name":"Wazowski","month_birth":6,"team":2,"created_at":"2022-11-05T20:25:50.441553Z"}'
### import io
### stream = io.BytesIO(content)
### data = JSONParser().parse(stream)
### deserializer = PersonSerializer(data=data)
### deserializer.is_valid()
True
### deserializer.fields
{'id': IntegerField(read_only=True), 'first_name': CharField(max_length=50, required=True), 'last_name': CharField(max_length=50, required=True), 'month_birth': ChoiceField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4,
 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1), 'team': PrimaryKeyRelatedField(queryset=<QuerySet [<Team: The Eagles (PL)>, <Team: T
he Chicago Bulls (US)>]>), 'created_at': DateTimeField()}
### deserializer.validated_data
OrderedDict([('first_name', 'Mike'), ('last_name', 'Wazowski'), ('month_birth', 6), ('team', <Team: The Eagles (PL)>), ('created_at', datetime.datetime(2022, 11, 5, 20, 25, 50, 441553, tzinfo=zoneinfo.ZoneInfo(key='UTC')))])

# Team
### from lab4.models import Team
### team = Team.objects.get(name="The Eagles")
### team 
<Team: The Eagles (PL)>
### team.id
2
### from lab4.serializers import TeamSerializer
### team_serializer = TeamSerializer(team)      
### team_serializer.data
{'id': 2, 'name': 'The Eagles', 'country': 'PL'}
### team_content = JSONRenderer().render(team_serializer.data)  
### team_content
b'{"id":2,"name":"The Eagles","country":"PL"}'
### team_stream = io.BytesIO(team_content)
### team_data = JSONParser().parse(team_stream)
### team_deserializer.fields
{'id': IntegerField(read_only=True), 'name': CharField(max_length=100, required=True), 'country': CharField(max_length=2, required=True)}
### team_deserializer.validated_data
OrderedDict([('name', 'The Eagles'), ('country', 'PL')])
