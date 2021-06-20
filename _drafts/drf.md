# drf
# _부분 업데이트_
### 기본적으로 serializer는 모든 필수 필드의 값을 전달해야합니다. 그렇지 않으면 유효성 검사 오류가 발생합니다.
partial### 부분 업데이트를 허용하기 위해 인수를 사용할 수 있습니다 .
# Update `comment` with partial data
serializer = CommentSerializer(comment, data={'content': 'foo bar'}, partial=True





### 중첩 된 표현이 선택적으로
None### 값을 받아 들일 수 있다면
required=False### 중첩 된 serializer에 플래그를 전달해야합니다 .
class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)  # May be an anonymous user.
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
### 마찬가지로 중첩 된 표현이 항목 목록이어야하는 경우
many=True### 플래그를 중첩 된 serializer에 전달해야합니다 .
class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    edits = EditItemSerializer(many=True)  # A nested list of 'edit' items.
    content = serializers.CharField(max_length=200)
    created = serializers.# 쓰기 가능한 중첩 표현
### 데이터 역 직렬화를 지원하는 중첩 된 표현을 처리 할 때 중첩 된 개체의 오류는 중첩 된 개체의 필드 이름 아래에 중첩됩니다.
serializer = CommentSerializer(data={'user': {'email': 'foobar', 'username': 'doe'}, 'content': 'baz'})
serializer.is_valid()
# False
serializer.errors
# {'user': {'email': ['Enter a valid e-mail address.']}, 'created': ['This field is required.']}
### 마찬가지로
.validated_data### 속성에는 중첩 된 데이터 구조가 포함됩니다.
.create()## 중첩 표현에 대한 작성 방법
### 쓰기 가능한 중첩 표현을 지원하는 경우 여러 개체 저장을 처리하는
.create()### 또는
.update()### 메서드 를 작성해야 합니다.
### 다음 예제는 중첩 된 프로필 개체를 사용하여 사용자 생성을 처리하는 방법을 보여줍니다.
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
.update()## 중첩 표현에 대한 작성 방법
### 업데이트의 경우 관계 업데이트를 처리하는 방법에 대해 신중하게 생각해야합니다. 예를 들어 관계에 대한 데이터가
None### 이거나 제공되지 않은 경우 다음 중 어떤 것이 발생해야합니까?
	* 	NULL### 데이터베이스에서 관계를 설정 합니다.
### 	* 	연관된 인스턴스를 삭제하십시오.
### 	* 	데이터를 무시하고 인스턴스를 그대로 둡니다.
### 	* 	유효성 검사 오류를 발생시킵니다.
### 다음은
.update()### 이전
UserSerializer### 클래스 의 메서드에 대한 예입니다 .
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.is_premium_member = profile_data.get(
            'is_premium_member',
            profile.is_premium_member
        )
        profile.has_support_contract = profile_data.get(
            'has_support_contract',
            profile.has_support_contract
         )
        profile.save()

        return instance
### 중첩 된 생성 및 업데이트의 동작이 모호 할 수 있고 관련 모델간에 복잡한 종속성이 필요할 수 있으므로 REST 프레임 워크 3에서는 항상 이러한 메서드를 명시 적으로 작성해야합니다. 기본값
ModelSerializer
.create()### 및
.update()### 메서드는 쓰기 가능한 중첩 표현에 대한 지원을 포함하지 않습니다.
### 그러나 자동 쓰기 가능 중첩 표현을 지원하는  DRF Writable Nested  와 같은 타사 패키지를 사용할 수 있습니다 .

[DRF Writable Nested](https://www.django-rest-framework.org/api-guide/serializers/#drf-writable-nested)









# 추가 컨텍스트 포함
### 직렬화되는 개체 외에도 직렬화기에 추가 컨텍스트를 제공해야하는 경우가 있습니다. 한 가지 일반적인 경우는 하이퍼 링크 된 관계를 포함하는 직렬 변환기를 사용하는 경우입니다. 직렬 변환기가 현재 요청에 액세스 할 수 있어야 정규화 된 URL을 제대로 생성 할 수 있습니다.
context### serializer를 인스턴스화 할 때 인수 를 전달하여 임의의 추가 컨텍스트를 제공 할 수 있습니다 . 예를 들면 :
serializer = AccountSerializer(account, context={'request': request})
serializer.data
# {'id': 6, 'owner': 'denvercoder9', 'created': datetime.datetime(2013, 2, 12, 09, 44, 56, 678870), 'details': 'http://example.com/accounts/6/details'}
### 컨텍스트 사전은 특성
.to_representation()### 에 액세스하여 사용자 지정 메서드 와 같은 serializer 필드 논리 내에서 사용할 수 있습니다
self.context### .




# BaseSerializer
BaseSerializer 대체 직렬화 및 역 직렬화 스타일을 쉽게 지원하는 데 사용할 수있는 클래스입니다.
이 클래스는 클래스와 동일한 기본 API를 구현합니다 Serializer.
	* 	.data -나가는 기본 표현을 반환합니다.
	* 	.is_valid() -들어오는 데이터를 역 직렬화하고 유효성을 검사합니다.
	* 	.validated_data -검증 된 수신 데이터를 반환합니다.
	* 	.errors -유효성 검사 중 오류를 반환합니다.
	* 	.save() -검증 된 데이터를 개체 인스턴스에 유지합니다.
serializer 클래스가 지원할 기능에 따라 재정의 할 수있는 네 가지 메서드가 있습니다.
	* 	.to_representation() -읽기 작업을 위해 직렬화를 지원하려면 이것을 재정의합니다.
	* 	.to_internal_value() -쓰기 작업에 대해 deserialization을 지원하려면이 값을 재정의합니다.
	* 	.create()및 .update()-인스턴스 저장을 지원하기 위해 이들 중 하나 또는 둘 다를 
	* 
	* 
	* 
	* 
	* 
	* 
	* 
	* 
	* data 에 파라미터가 주어지면 다음과 같은 과정을 거치게 됩니다.
		serializer.is_valid() 가 호출 되었을 시,
		serializer.initial_data 에 data 값을 넣어주고
		serializer.validated_data 에 유효성 검증을 통과한 값들을 넣어주고 serializer.save() 시 이 값들을 저장하게 된다.
		serializer.errors 에는 유효성 검사에서의 오류들이
		serializer.data 에는 유효성 검사 후 인스턴스 값이 사전으로 저장된다.

https://ssungkang.tistory.com/entry/Django-Serializer-%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%82%AC-%EB%B0%8F-%EC%A0%80%EC%9E%A5



::::












