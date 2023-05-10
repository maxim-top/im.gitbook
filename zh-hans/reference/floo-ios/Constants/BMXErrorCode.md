# BMXErrorCode Constants Reference

  **Declared in** floo_proxy.h  

### BMXErrorCode

错误码

BMXErrorCode_NoError:
&ldquo;The operation was performed successfully without error.&rdquo;
BMXErrorCode_GeneralError:
&ldquo;A generic error occurred during operation execution.&rdquo;
BMXErrorCode_InvalidParam:
&ldquo;There are invalid parameters in the input parameters.&rdquo;
BMXErrorCode_NotFound:
&ldquo;The path or file does not exist.&rdquo;
BMXErrorCode_DbOperationFailed:
&ldquo;The local database operation failed.&rdquo;
BMXErrorCode_SignInCancelled:
&ldquo;The user has cancelled the login operation.&rdquo;
BMXErrorCode_SignInTimeout:
&ldquo;The user login operation has timed out.&rdquo;
BMXErrorCode_SignInFailed:
&ldquo;The user login operation has failed.&rdquo;
BMXErrorCode_UserNotLogin:
&ldquo;The user hasn&rsquo;t logged in yet.&rdquo;
BMXErrorCode_UserAlreadyLogin:
&ldquo;Other user has logged in.&rdquo;
BMXErrorCode_UserAuthFailed:
&ldquo;User authentication failed, username/id or password is incorrect.&rdquo;
BMXErrorCode_UserPermissionDenied:
&ldquo;The user does not have permission to perform this action.&rdquo;
BMXErrorCode_UserNotExist:
&ldquo;The user does not exist.&rdquo;
BMXErrorCode_UserAlreadyExist:
&ldquo;The user is already exist.&rdquo;
BMXErrorCode_UserFrozen:
&ldquo;The user has been frozen.&rdquo;
BMXErrorCode_UserBanned:
&ldquo;The use has been banned from sending messages.&rdquo;
BMXErrorCode_UserRemoved:
&ldquo;The user has been removed.&rdquo;
BMXErrorCode_UserTooManyDevice:
&ldquo;The use has logged into too many devices.&rdquo;
BMXErrorCode_UserPasswordChanged:
&ldquo;The user has changed passwords on other device.&rdquo;
BMXErrorCode_UserKickedBySameDevice:
&ldquo;The user is kicked out by the same device.&rdquo;
BMXErrorCode_UserKickedByOtherDevices:
&ldquo;The user is kicked out by other device.&rdquo;
BMXErrorCode_UserAbnormal:
&ldquo;The user login status is not normal, the user is advised to login again.&rdquo;
BMXErrorCode_UserCancel:
&ldquo;The user has cancelled the operation.&rdquo;
BMXErrorCode_UserOldPasswordNotMatch:
&ldquo;The old password does not match when the password is changed.&rdquo;
BMXErrorCode_UserSigningIn:
&ldquo;The user is signning in.&rdquo;
BMXErrorCode_PushTokenInvalid:
&ldquo;The push token is not valid.&rdquo;
BMXErrorCode_PushAliasBindByOtherUser:
&ldquo;The push alias is bound by other user.&rdquo;
BMXErrorCode_PushAliasTokenNotMatch:
&ldquo;The push alias does not match the token.&rdquo;
BMXErrorCode_InvalidVerificationCode:
&ldquo;The verification code is not valid.&rdquo;
BMXErrorCode_InvalidRequestParameter:
&ldquo;The request parameters are not valid.&rdquo;
BMXErrorCode_InvalidUserNameParameter:
&ldquo;The username parameter is not valid.&rdquo;
BMXErrorCode_MissingAccessToken:
&ldquo;The access token parameter is missing.&rdquo;
BMXErrorCode_CurrentUserIsInRoster:
&ldquo;The current user is already in the roster list.&rdquo;
BMXErrorCode_CurrentUserIsInBlocklist:
&ldquo;The current user is already in the blocked list.&rdquo;
BMXErrorCode_AnswerFailed:
&ldquo;The application does not exist or has already expired.&rdquo;
BMXErrorCode_InvalidToken:
&ldquo;The current token is not valid.&rdquo;
BMXErrorCode_InvalidFileSign:
&ldquo;The current file signature is not valid.&rdquo;
BMXErrorCode_InvalidFileObjectType:
&ldquo;The current file object type is not valid.&rdquo;
BMXErrorCode_InvalidFileUploadToType:
&ldquo;The to type of the uploaded file is not valid.&rdquo;
BMXErrorCode_InvalidFileDownloadUrl:
&ldquo;The file download url is not valid.&rdquo;
BMXErrorCode_MessageInvalid:
&ldquo;The current message format is not valid.&rdquo;
BMXErrorCode_MessageOutRecallTime:
&ldquo;The current message has exceeded the allowed recall time.&rdquo;
BMXErrorCode_MessageRecallDisabled:
&ldquo;The current message is not recallable.&rdquo;
BMXErrorCode_MessageCensored:
&ldquo;The current message include censored content.&rdquo;
BMXErrorCode_MessageInvalidType:
&ldquo;This operation is not supported by the current message type.&rdquo;
BMXErrorCode_MessageBadArg:
&ldquo;The current message contains illegal characters.&rdquo;
BMXErrorCode_MessageRateLimitExceeded:
&ldquo;The message sending frequency has reached the limit.&rdquo;
BMXErrorCode_RosterNotFriend:
&ldquo;The current roster is not a friend.&rdquo;
BMXErrorCode_RosterBlockListExist:
&ldquo;The current roster is already on the blocklist.&rdquo;
BMXErrorCode_RosterRejectApplication:
&ldquo;The current user does not accept any application.&rdquo;
BMXErrorCode_RosterHasDeletedFromSystem:
&ldquo;The current roster has been deleted from the system.&rdquo;
BMXErrorCode_GroupServerDbError:
&ldquo;An error occurred in the server database.&rdquo;
BMXErrorCode_GroupNotExist:
&ldquo;The Specified group not found.&rdquo;
BMXErrorCode_GroupNotMemberFound:
&ldquo;The user is not in the specified group.&rdquo;
BMXErrorCode_GroupMsgNotifyTypeUnknown:
&ldquo;The group message notification type is unknown.&rdquo;
BMXErrorCode_GroupOwnerCannotLeave:
&ldquo;The group owner cannot leave the group.&rdquo;
BMXErrorCode_GroupTransferNotAllowed:
&ldquo;Group owners can only be transferred to group members. The currently specified user is not a group member.&rdquo;
BMXErrorCode_GroupRecoveryMode:
&ldquo;Group is recovery mode.&rdquo;
BMXErrorCode_GroupExceedLimitGlobal:
&ldquo;The number of global groups reaches the limit.&rdquo;
BMXErrorCode_GroupExceedLimitUserCreate:
&ldquo;The number of incoming members reached the limit when the group was created.&rdquo;
BMXErrorCode_GroupExceedLimitUserJoin:
&ldquo;The number of group members has reached the limit.&rdquo;
BMXErrorCode_GroupCapacityExceedLimit:
&ldquo;The maximum group capacity is limited.&rdquo;
BMXErrorCode_GroupMemberPermissionRequired:
&ldquo;This operation needs group member permission.&rdquo;
BMXErrorCode_GroupAdminPermissionRequired:
&ldquo;This operation needs group admin permission.&rdquo;
BMXErrorCode_GroupOwnerPermissionRequired:
&ldquo;This operation needs group owner permission.&rdquo;
BMXErrorCode_GroupApplicationExpiredOrHandled:
&ldquo;The current group application has expired or be handled.&rdquo;
BMXErrorCode_GroupInvitationExpiredOrHandled:
&ldquo;The current group invitation  has expired or be handled.&rdquo;
BMXErrorCode_GroupKickTooManyTimes:
&ldquo;The current user has been kicked more than 3 times.&rdquo;
BMXErrorCode_GroupMemberExist:
&ldquo;The current user is already in the group.&rdquo;
BMXErrorCode_GroupBlockListExist:
&ldquo;The current user is already in group blocklist.&rdquo;
BMXErrorCode_GroupAnnouncementNotFound:
&ldquo;The current group announcement with the specified id was not found.&rdquo;
BMXErrorCode_GroupAnnouncementForbidden:
&ldquo;Group announcement has been forbidden by system admin.&rdquo;
BMXErrorCode_GroupSharedFileNotFound:
&ldquo;Group shared file is not found.&rdquo;
BMXErrorCode_GroupSharedFileOperateNotAllowed:
&ldquo;Do not have permission to operate group shared files.&rdquo;
BMXErrorCode_GroupMemberBanned:
&ldquo;Group banned member to send message.&rdquo;
BMXErrorCode_ServerNotReachable:
&ldquo;The current server not reachable.&rdquo;
BMXErrorCode_ServerUnknownError:
&ldquo;An unknown error occurred on the server.&rdquo;
BMXErrorCode_ServerInvalid:
&ldquo;The current server host is not valid.&rdquo;
BMXErrorCode_ServerDecryptionFailed:
&ldquo;A decryption failed error occurred on the server.&rdquo;
BMXErrorCode_ServerEncryptMethodUnsupported:
&ldquo;The server does not currently support the specified encryption method.&rdquo;
BMXErrorCode_ServerBusy:
&ldquo;The server is currently busy.&rdquo;
BMXErrorCode_ServerNeedRetry:
&ldquo;The server needs to retry.&rdquo;
BMXErrorCode_ServerTimeOut:
&ldquo;A timeout error occurred on the server.&rdquo;
BMXErrorCode_ServerConnectFailed:
&ldquo;A connection failure error occurred on the server.&rdquo;
BMXErrorCode_ServerDNSFailed:
&ldquo;The current server failed to obtain the dns list.&rdquo;
BMXErrorCode_ServerNeedReconnected:
&ldquo;The current server has changed and needs to be reconnected.&rdquo;
BMXErrorCode_ServerFileUploadUnknownError:
&ldquo;An unknown file upload error occurred on the server.&rdquo;
BMXErrorCode_ServerFileDownloadUnknownError:
&ldquo;An unknown file download error occurred on the server.&rdquo;
BMXErrorCode_ServerInvalidLicense:
&ldquo;An invalid license error occurred on the server.&rdquo;
BMXErrorCode_ServerLicenseLimit:
&ldquo;A license limit error occurred on the server.&rdquo;
BMXErrorCode_ServerAppFrozen:
&ldquo;An app freeze error occurred on the server.&rdquo;
BMXErrorCode_ServerTooManyRequest:
&ldquo;The server is being accessed too many times.&rdquo;
BMXErrorCode_ServerNotAllowOpenRegister:
&ldquo;The server is not allowed open registration.&rdquo;
BMXErrorCode_ServerFireplaceUnknownError:
&ldquo;An unknown error occurred on the fireplace server.&rdquo;
BMXErrorCode_ServerResponseInvalid:
&ldquo;The current response returned by the server is not valid.&rdquo;
BMXErrorCode_ServerInvalidUploadUrl:
&ldquo;The current upload server url is not valid.&rdquo;
BMXErrorCode_ServerAppLicenseInvalid:
&ldquo;The current server app license is not valid.&rdquo;
BMXErrorCode_ServerAppLicenseExpired:
&ldquo;The current server app license has expired.&rdquo;
BMXErrorCode_ServerAppLicenseExceedLimit:
&ldquo;The current server app license has reached its limit.&rdquo;
BMXErrorCode_ServerAppIdMissing:
&ldquo;The current server appid is missing.&rdquo;
BMXErrorCode_ServerAppIdInvalid:
&ldquo;The current server appid is not valid.&rdquo;
BMXErrorCode_ServerAppSignInvalid:
&ldquo;The current server app signature is not valid.&rdquo;
BMXErrorCode_ServerAppNotifierNotExist:
&ldquo;The current server app notifier not exist.&rdquo;
BMXErrorCode_ServerNoClusterInfoForClusterId:
&ldquo;The specified cluster id has no cluster information.&rdquo;
BMXErrorCode_ServerFileDownloadFailure:
&ldquo;A download error occurred on the server.&rdquo;
BMXErrorCode_ServerAppStatusNotNormal:
&ldquo;The current status of the server app is not normal.&rdquo;
BMXErrorCode_ServerPlatformNotAllowed:
&ldquo;The server does not support the currently logged in device platform.&rdquo;
BMXErrorCode_ServerCannotCreateDeviceSn:
&ldquo;The server cannot generate the serial number of the currently logged in device.&rdquo;
BMXErrorCode_ServerRtcNotOpen:
&ldquo;The RTC service is not open.&rdquo;

#### Definition
    typedef NS_ENUM(NSInteger, BMXErrorCode ) {   
        
        BMXErrorCode_NoError,
        
        BMXErrorCode_GeneralError,
        
        BMXErrorCode_InvalidParam,
        
        BMXErrorCode_NotFound,
        
        BMXErrorCode_DbOperationFailed,
        
        BMXErrorCode_SignInCancelled,
        
        BMXErrorCode_SignInTimeout,
        
        BMXErrorCode_SignInFailed,
        
        BMXErrorCode_UserNotLogin = 100,
        
        BMXErrorCode_UserAlreadyLogin,
        
        BMXErrorCode_UserAuthFailed,
        
        BMXErrorCode_UserPermissionDenied,
        
        BMXErrorCode_UserNotExist,
        
        BMXErrorCode_UserAlreadyExist,
        
        BMXErrorCode_UserFrozen,
        
        BMXErrorCode_UserBanned,
        
        BMXErrorCode_UserRemoved,
        
        BMXErrorCode_UserTooManyDevice,
        
        BMXErrorCode_UserPasswordChanged,
        
        BMXErrorCode_UserKickedBySameDevice,
        
        BMXErrorCode_UserKickedByOtherDevices,
        
        BMXErrorCode_UserAbnormal,
        
        BMXErrorCode_UserCancel,
        
        BMXErrorCode_UserOldPasswordNotMatch,
        
        BMXErrorCode_UserSigningIn,
        
        BMXErrorCode_PushTokenInvalid = 200,
        
        BMXErrorCode_PushAliasBindByOtherUser,
        
        BMXErrorCode_PushAliasTokenNotMatch,
        
        BMXErrorCode_InvalidVerificationCode = 300,
        
        BMXErrorCode_InvalidRequestParameter,
        
        BMXErrorCode_InvalidUserNameParameter,
        
        BMXErrorCode_MissingAccessToken,
        
        BMXErrorCode_CurrentUserIsInRoster,
        
        BMXErrorCode_CurrentUserIsInBlocklist,
        
        BMXErrorCode_AnswerFailed,
        
        BMXErrorCode_InvalidToken,
        
        BMXErrorCode_InvalidFileSign,
        
        BMXErrorCode_InvalidFileObjectType,
        
        BMXErrorCode_InvalidFileUploadToType,
        
        BMXErrorCode_InvalidFileDownloadUrl,
        
        BMXErrorCode_MessageInvalid = 400,
        
        BMXErrorCode_MessageOutRecallTime,
        
        BMXErrorCode_MessageRecallDisabled,
        
        BMXErrorCode_MessageCensored,
        
        BMXErrorCode_MessageInvalidType,
        
        BMXErrorCode_MessageBadArg,
        
        BMXErrorCode_MessageRateLimitExceeded,
        
        BMXErrorCode_RosterNotFriend = 500,
        
        BMXErrorCode_RosterBlockListExist,
        
        BMXErrorCode_RosterRejectApplication,
        
        BMXErrorCode_RosterHasDeletedFromSystem,
        
        BMXErrorCode_GroupServerDbError = 600,
        
        BMXErrorCode_GroupNotExist,
        
        BMXErrorCode_GroupNotMemberFound,
        
        BMXErrorCode_GroupMsgNotifyTypeUnknown,
        
        BMXErrorCode_GroupOwnerCannotLeave,
        
        BMXErrorCode_GroupTransferNotAllowed,
        
        BMXErrorCode_GroupRecoveryMode,
        
        BMXErrorCode_GroupExceedLimitGlobal,
        
        BMXErrorCode_GroupExceedLimitUserCreate,
        
        BMXErrorCode_GroupExceedLimitUserJoin,
        
        BMXErrorCode_GroupCapacityExceedLimit,
        
        BMXErrorCode_GroupMemberPermissionRequired,
        
        BMXErrorCode_GroupAdminPermissionRequired,
        
        BMXErrorCode_GroupOwnerPermissionRequired,
        
        BMXErrorCode_GroupApplicationExpiredOrHandled,
        
        BMXErrorCode_GroupInvitationExpiredOrHandled,
        
        BMXErrorCode_GroupKickTooManyTimes,
        
        BMXErrorCode_GroupMemberExist,
        
        BMXErrorCode_GroupBlockListExist,
        
        BMXErrorCode_GroupAnnouncementNotFound,
        
        BMXErrorCode_GroupAnnouncementForbidden,
        
        BMXErrorCode_GroupSharedFileNotFound,
        
        BMXErrorCode_GroupSharedFileOperateNotAllowed,
        
        BMXErrorCode_GroupMemberBanned,
        
        BMXErrorCode_ServerNotReachable = 700,
        
        BMXErrorCode_ServerUnknownError,
        
        BMXErrorCode_ServerInvalid,
        
        BMXErrorCode_ServerDecryptionFailed,
        
        BMXErrorCode_ServerEncryptMethodUnsupported,
        
        BMXErrorCode_ServerBusy,
        
        BMXErrorCode_ServerNeedRetry,
        
        BMXErrorCode_ServerTimeOut,
        
        BMXErrorCode_ServerConnectFailed,
        
        BMXErrorCode_ServerDNSFailed,
        
        BMXErrorCode_ServerNeedReconnected,
        
        BMXErrorCode_ServerFileUploadUnknownError,
        
        BMXErrorCode_ServerFileDownloadUnknownError,
        
        BMXErrorCode_ServerInvalidLicense,
        
        BMXErrorCode_ServerLicenseLimit,
        
        BMXErrorCode_ServerAppFrozen,
        
        BMXErrorCode_ServerTooManyRequest,
        
        BMXErrorCode_ServerNotAllowOpenRegister,
        
        BMXErrorCode_ServerFireplaceUnknownError,
        
        BMXErrorCode_ServerResponseInvalid,
        
        BMXErrorCode_ServerInvalidUploadUrl,
        
        BMXErrorCode_ServerAppLicenseInvalid,
        
        BMXErrorCode_ServerAppLicenseExpired,
        
        BMXErrorCode_ServerAppLicenseExceedLimit,
        
        BMXErrorCode_ServerAppIdMissing,
        
        BMXErrorCode_ServerAppIdInvalid,
        
        BMXErrorCode_ServerAppSignInvalid,
        
        BMXErrorCode_ServerAppNotifierNotExist,
        
        BMXErrorCode_ServerNoClusterInfoForClusterId,
        
        BMXErrorCode_ServerFileDownloadFailure,
        
        BMXErrorCode_ServerAppStatusNotNormal,
        
        BMXErrorCode_ServerPlatformNotAllowed,
        
        BMXErrorCode_ServerCannotCreateDeviceSn,
        
        BMXErrorCode_ServerRtcNotOpen,
        
    };

#### Constants

<a name="" title="BMXErrorCode_NoError"></a><code>BMXErrorCode_NoError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GeneralError"></a><code>BMXErrorCode_GeneralError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidParam"></a><code>BMXErrorCode_InvalidParam</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_NotFound"></a><code>BMXErrorCode_NotFound</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_DbOperationFailed"></a><code>BMXErrorCode_DbOperationFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_SignInCancelled"></a><code>BMXErrorCode_SignInCancelled</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_SignInTimeout"></a><code>BMXErrorCode_SignInTimeout</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_SignInFailed"></a><code>BMXErrorCode_SignInFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserNotLogin"></a><code>BMXErrorCode_UserNotLogin</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserAlreadyLogin"></a><code>BMXErrorCode_UserAlreadyLogin</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserAuthFailed"></a><code>BMXErrorCode_UserAuthFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserPermissionDenied"></a><code>BMXErrorCode_UserPermissionDenied</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserNotExist"></a><code>BMXErrorCode_UserNotExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserAlreadyExist"></a><code>BMXErrorCode_UserAlreadyExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserFrozen"></a><code>BMXErrorCode_UserFrozen</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserBanned"></a><code>BMXErrorCode_UserBanned</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserRemoved"></a><code>BMXErrorCode_UserRemoved</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserTooManyDevice"></a><code>BMXErrorCode_UserTooManyDevice</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserPasswordChanged"></a><code>BMXErrorCode_UserPasswordChanged</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserKickedBySameDevice"></a><code>BMXErrorCode_UserKickedBySameDevice</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserKickedByOtherDevices"></a><code>BMXErrorCode_UserKickedByOtherDevices</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserAbnormal"></a><code>BMXErrorCode_UserAbnormal</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserCancel"></a><code>BMXErrorCode_UserCancel</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserOldPasswordNotMatch"></a><code>BMXErrorCode_UserOldPasswordNotMatch</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_UserSigningIn"></a><code>BMXErrorCode_UserSigningIn</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_PushTokenInvalid"></a><code>BMXErrorCode_PushTokenInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_PushAliasBindByOtherUser"></a><code>BMXErrorCode_PushAliasBindByOtherUser</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_PushAliasTokenNotMatch"></a><code>BMXErrorCode_PushAliasTokenNotMatch</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidVerificationCode"></a><code>BMXErrorCode_InvalidVerificationCode</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidRequestParameter"></a><code>BMXErrorCode_InvalidRequestParameter</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidUserNameParameter"></a><code>BMXErrorCode_InvalidUserNameParameter</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MissingAccessToken"></a><code>BMXErrorCode_MissingAccessToken</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_CurrentUserIsInRoster"></a><code>BMXErrorCode_CurrentUserIsInRoster</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_CurrentUserIsInBlocklist"></a><code>BMXErrorCode_CurrentUserIsInBlocklist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_AnswerFailed"></a><code>BMXErrorCode_AnswerFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidToken"></a><code>BMXErrorCode_InvalidToken</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidFileSign"></a><code>BMXErrorCode_InvalidFileSign</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidFileObjectType"></a><code>BMXErrorCode_InvalidFileObjectType</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidFileUploadToType"></a><code>BMXErrorCode_InvalidFileUploadToType</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_InvalidFileDownloadUrl"></a><code>BMXErrorCode_InvalidFileDownloadUrl</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageInvalid"></a><code>BMXErrorCode_MessageInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageOutRecallTime"></a><code>BMXErrorCode_MessageOutRecallTime</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageRecallDisabled"></a><code>BMXErrorCode_MessageRecallDisabled</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageCensored"></a><code>BMXErrorCode_MessageCensored</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageInvalidType"></a><code>BMXErrorCode_MessageInvalidType</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageBadArg"></a><code>BMXErrorCode_MessageBadArg</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_MessageRateLimitExceeded"></a><code>BMXErrorCode_MessageRateLimitExceeded</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_RosterNotFriend"></a><code>BMXErrorCode_RosterNotFriend</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_RosterBlockListExist"></a><code>BMXErrorCode_RosterBlockListExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_RosterRejectApplication"></a><code>BMXErrorCode_RosterRejectApplication</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_RosterHasDeletedFromSystem"></a><code>BMXErrorCode_RosterHasDeletedFromSystem</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupServerDbError"></a><code>BMXErrorCode_GroupServerDbError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupNotExist"></a><code>BMXErrorCode_GroupNotExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupNotMemberFound"></a><code>BMXErrorCode_GroupNotMemberFound</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupMsgNotifyTypeUnknown"></a><code>BMXErrorCode_GroupMsgNotifyTypeUnknown</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupOwnerCannotLeave"></a><code>BMXErrorCode_GroupOwnerCannotLeave</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupTransferNotAllowed"></a><code>BMXErrorCode_GroupTransferNotAllowed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupRecoveryMode"></a><code>BMXErrorCode_GroupRecoveryMode</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupExceedLimitGlobal"></a><code>BMXErrorCode_GroupExceedLimitGlobal</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupExceedLimitUserCreate"></a><code>BMXErrorCode_GroupExceedLimitUserCreate</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupExceedLimitUserJoin"></a><code>BMXErrorCode_GroupExceedLimitUserJoin</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupCapacityExceedLimit"></a><code>BMXErrorCode_GroupCapacityExceedLimit</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupMemberPermissionRequired"></a><code>BMXErrorCode_GroupMemberPermissionRequired</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupAdminPermissionRequired"></a><code>BMXErrorCode_GroupAdminPermissionRequired</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupOwnerPermissionRequired"></a><code>BMXErrorCode_GroupOwnerPermissionRequired</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupApplicationExpiredOrHandled"></a><code>BMXErrorCode_GroupApplicationExpiredOrHandled</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupInvitationExpiredOrHandled"></a><code>BMXErrorCode_GroupInvitationExpiredOrHandled</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupKickTooManyTimes"></a><code>BMXErrorCode_GroupKickTooManyTimes</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupMemberExist"></a><code>BMXErrorCode_GroupMemberExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupBlockListExist"></a><code>BMXErrorCode_GroupBlockListExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupAnnouncementNotFound"></a><code>BMXErrorCode_GroupAnnouncementNotFound</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupAnnouncementForbidden"></a><code>BMXErrorCode_GroupAnnouncementForbidden</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupSharedFileNotFound"></a><code>BMXErrorCode_GroupSharedFileNotFound</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupSharedFileOperateNotAllowed"></a><code>BMXErrorCode_GroupSharedFileOperateNotAllowed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_GroupMemberBanned"></a><code>BMXErrorCode_GroupMemberBanned</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerNotReachable"></a><code>BMXErrorCode_ServerNotReachable</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerUnknownError"></a><code>BMXErrorCode_ServerUnknownError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerInvalid"></a><code>BMXErrorCode_ServerInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerDecryptionFailed"></a><code>BMXErrorCode_ServerDecryptionFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerEncryptMethodUnsupported"></a><code>BMXErrorCode_ServerEncryptMethodUnsupported</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerBusy"></a><code>BMXErrorCode_ServerBusy</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerNeedRetry"></a><code>BMXErrorCode_ServerNeedRetry</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerTimeOut"></a><code>BMXErrorCode_ServerTimeOut</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerConnectFailed"></a><code>BMXErrorCode_ServerConnectFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerDNSFailed"></a><code>BMXErrorCode_ServerDNSFailed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerNeedReconnected"></a><code>BMXErrorCode_ServerNeedReconnected</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerFileUploadUnknownError"></a><code>BMXErrorCode_ServerFileUploadUnknownError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerFileDownloadUnknownError"></a><code>BMXErrorCode_ServerFileDownloadUnknownError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerInvalidLicense"></a><code>BMXErrorCode_ServerInvalidLicense</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerLicenseLimit"></a><code>BMXErrorCode_ServerLicenseLimit</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppFrozen"></a><code>BMXErrorCode_ServerAppFrozen</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerTooManyRequest"></a><code>BMXErrorCode_ServerTooManyRequest</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerNotAllowOpenRegister"></a><code>BMXErrorCode_ServerNotAllowOpenRegister</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerFireplaceUnknownError"></a><code>BMXErrorCode_ServerFireplaceUnknownError</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerResponseInvalid"></a><code>BMXErrorCode_ServerResponseInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerInvalidUploadUrl"></a><code>BMXErrorCode_ServerInvalidUploadUrl</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppLicenseInvalid"></a><code>BMXErrorCode_ServerAppLicenseInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppLicenseExpired"></a><code>BMXErrorCode_ServerAppLicenseExpired</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppLicenseExceedLimit"></a><code>BMXErrorCode_ServerAppLicenseExceedLimit</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppIdMissing"></a><code>BMXErrorCode_ServerAppIdMissing</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppIdInvalid"></a><code>BMXErrorCode_ServerAppIdInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppSignInvalid"></a><code>BMXErrorCode_ServerAppSignInvalid</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppNotifierNotExist"></a><code>BMXErrorCode_ServerAppNotifierNotExist</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerNoClusterInfoForClusterId"></a><code>BMXErrorCode_ServerNoClusterInfoForClusterId</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerFileDownloadFailure"></a><code>BMXErrorCode_ServerFileDownloadFailure</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerAppStatusNotNormal"></a><code>BMXErrorCode_ServerAppStatusNotNormal</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerPlatformNotAllowed"></a><code>BMXErrorCode_ServerPlatformNotAllowed</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerCannotCreateDeviceSn"></a><code>BMXErrorCode_ServerCannotCreateDeviceSn</code>

错误码

   Declared In `floo_proxy.h`.

<a name="" title="BMXErrorCode_ServerRtcNotOpen"></a><code>BMXErrorCode_ServerRtcNotOpen</code>

错误码

   Declared In `floo_proxy.h`.

#### Declared In
`floo_proxy.h`

