# Table of contents

* [即时通讯开发指南（IM）](README.md)
* [快速开发](quick-start/README.md)
  * [iOS 客户端快速开发（floo-ios）](quick-start/floo-ios-quick-start.md)
  * [安卓客户端快速开发（floo-android）](quick-start/floo-android-quick-start.md)
  * [Linux/C++ 客户端快速开发（floo）](quick-start/floo-quick-start.md)
  * [Web 前端快速开发（floo-web）](quick-start/floo-web-quick-start.md)
  * [服务端开发指南（server api）](quick-start/server-api-quick-start.md)
  * [推送开发指南（PUSH）](quick-start/push-dev-guide.md)
  * [私有云部署文档](quick-start/how-to-deploy-private-cloud.md)
* [详细文档](reference/README.md)
  * [floo-web API介绍](reference/floo-web.md)
  * [floo API](reference/floo.md)
    * **class [floo::BMXChatService](reference/floo/classfloo_1_1_b_m_x_chat_service.md)** <br>聊天Service 
    * **class [floo::BMXChatServiceListener](reference/floo/classfloo_1_1_b_m_x_chat_service_listener.md)** <br>聊天监听者 
    * **class [floo::BMXClient](reference/floo/classfloo_1_1_b_m_x_client.md)** <br>客户端 
    * **class [floo::BMXConversation](reference/floo/classfloo_1_1_b_m_x_conversation.md)** <br>会话 
    * **class [floo::BMXDevice](reference/floo/classfloo_1_1_b_m_x_device.md)** <br>设备信息 
    * **class [floo::BMXError](reference/floo/classfloo_1_1_b_m_x_error.md)** 
    * **class [floo::BMXFileAttachment](reference/floo/classfloo_1_1_b_m_x_file_attachment.md)** <br>消息文件附件 
    * **class [floo::BMXForwardAttachment](reference/floo/classfloo_1_1_b_m_x_forward_attachment.md)** <br>消息转发附件 
      * **class [Message](reference/floo/classfloo_1_1_b_m_x_forward_attachment_1_1_message.md)** <br>转发消息附件自定义消息 
    * **class [floo::BMXGroup](reference/floo/classfloo_1_1_b_m_x_group.md)** <br>群组 
    * **class [floo::BMXGroupService](reference/floo/classfloo_1_1_b_m_x_group_service.md)** <br>群组Service 
    * **class [floo::BMXGroupServiceListener](reference/floo/classfloo_1_1_b_m_x_group_service_listener.md)** <br>群组变化监听者 
    * **class [floo::BMXImageAttachment](reference/floo/classfloo_1_1_b_m_x_image_attachment.md)** <br>图片消息附件 
    * **class [floo::BMXLocationAttachment](reference/floo/classfloo_1_1_b_m_x_location_attachment.md)** <br>位置消息附件 
    * **class [floo::BMXMessage](reference/floo/classfloo_1_1_b_m_x_message.md)** <br>消息 
    * **class [floo::BMXMessageAttachment](reference/floo/classfloo_1_1_b_m_x_message_attachment.md)** <br>消息附件 
    * **class [floo::BMXMessageConfig](reference/floo/classfloo_1_1_b_m_x_message_config.md)** <br>消息配置 
    * **class [floo::BMXNetworkListener](reference/floo/classfloo_1_1_b_m_x_network_listener.md)** 
    * **class [floo::BMXPushService](reference/floo/classfloo_1_1_b_m_x_push_service.md)** 
    * **class [floo::BMXPushServiceListener](reference/floo/classfloo_1_1_b_m_x_push_service_listener.md)** 
    * **class [floo::BMXPushUserProfile](reference/floo/classfloo_1_1_b_m_x_push_user_profile.md)** <br>Push用户Profile. 
    * **class [floo::BMXResultPage](reference/floo/classfloo_1_1_b_m_x_result_page.md)** <br>分页结果 
    * **class [floo::BMXRosterItem](reference/floo/classfloo_1_1_b_m_x_roster_item.md)** <br>联系人 
    * **class [floo::BMXRosterService](reference/floo/classfloo_1_1_b_m_x_roster_service.md)** <br>好友Service 
    * **class [floo::BMXRosterServiceListener](reference/floo/classfloo_1_1_b_m_x_roster_service_listener.md)** <br>好友变化监听者 
    * **class [floo::BMXSDKConfig](reference/floo/classfloo_1_1_b_m_x_s_d_k_config.md)** <br>SDK设置管理 
    * **class [floo::BMXUserProfile](reference/floo/classfloo_1_1_b_m_x_user_profile.md)** <br>用户Profile 
    * **class [floo::BMXUserService](reference/floo/classfloo_1_1_b_m_x_user_service.md)** <br>用户Service 
    * **class [floo::BMXUserServiceListener](reference/floo/classfloo_1_1_b_m_x_user_service_listener.md)** <br>用户状态监听者 
    * **class [floo::BMXVideoAttachment](reference/floo/classfloo_1_1_b_m_x_video_attachment.md)** <br>视频消息附件 
    * **class [floo::BMXVoiceAttachment](reference/floo/classfloo_1_1_b_m_x_voice_attachment.md)** <br>音频消息附件 
  * [floo android API](reference/floo-android.md)
    * **class [im::floo::floolib::BMXChatManager](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)** <br>聊天管理器 
    * **class [im::floo::floolib::BMXChatService](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)** <br>聊天Service 
    * **class [im::floo::floolib::BMXChatServiceListener](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md)** <br>聊天监听者 
    * **class [im::floo::floolib::BMXClient](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_client.md)** <br>客户端 
    * **class [im::floo::floolib::BMXConversation](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md)** <br>会话 
    * **class [im::floo::floolib::BMXDevice](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_device.md)** <br>设备信息 
    * **class [im::floo::floolib::BMXFileAttachment](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)** <br>消息文件附件 
    * **class [im::floo::floolib::BMXGroup](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group.md)** <br>群组 
      * **class [Announcement](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_announcement.md)** <br>群公告 
      * **class [Application](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_application.md)** <br>群申请 
    * **class [im::floo::floolib::BMXGroup::BannedMember](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_banned_member.md)** <br>群禁言成员 
    * **class [im::floo::floolib::BMXGroup::Invitation](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_invitation.md)** <br>群邀请 
    * **class [im::floo::floolib::BMXGroup::Member](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_member.md)** <br>群成员 
    * **class [im::floo::floolib::BMXGroup::SharedFile](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_shared_file.md)** <br>群共享文件 
    * **class [im::floo::floolib::BMXGroupManager](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)** <br>群组管理器 
    * **class [im::floo::floolib::BMXGroupService](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)** <br>群组Service 
      * **class [CreateGroupOptions](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_1_1_create_group_options.md)** <br>创建群组选项 
    * **class [im::floo::floolib::BMXGroupServiceListener](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md)** <br>群组变化监听者 
    * **class [im::floo::floolib::BMXImageAttachment](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md)** <br>图片消息附件 
    * **class [im::floo::floolib::BMXLocationAttachment](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md)** <br>位置消息附件 
    * **class [im::floo::floolib::BMXMessage](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)** <br>消息 
    * **class [im::floo::floolib::BMXMessageAttachment](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)** <br>消息附件 
    * **class [im::floo::floolib::BMXMessageAttachment::Size](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment_1_1_size.md)** <br>图片/视频大小 
    * **class [im::floo::floolib::BMXMessageConfig](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md)** <br>消息配置 
    * **class [im::floo::floolib::BMXNetworkListener](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)** <br>网络监听者 
    * **class [im::floo::floolib::BMXPushManager](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md)** <br>推送管理器 
    * **class [im::floo::floolib::BMXPushService](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)** 
    * **class [im::floo::floolib::BMXPushServiceListener](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md)** 
    * **class [im::floo::floolib::BMXPushUserProfile](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md)** 
      * **class [MessagePushSetting](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile_1_1_message_push_setting.md)** 
    * **class [im::floo::floolib::BMXRosterItem](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md)** <br>联系人 
    * **class [im::floo::floolib::BMXRosterManager](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md)** <br>好友管理器 
    * **class [im::floo::floolib::BMXRosterService](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md)** <br>好友Service 
      * **class [Application](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_1_1_application.md)** <br>好友邀请 
    * **class [im::floo::floolib::BMXRosterServiceListener](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md)** <br>好友变化监听者 
    * **class [im::floo::floolib::BMXSDKConfig](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md)** <br>SDK设置管理 
      * **class [HostConfig](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config_1_1_host_config.md)** 
    * **class [im::floo::floolib::BMXUserManager](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)** <br>用户管理器 
    * **class [im::floo::floolib::BMXUserProfile](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md)** <br>用户Profile 
    * **class [im::floo::floolib::BMXUserProfile::AuthQuestion](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile_1_1_auth_question.md)** <br>添加好友时的校验问题 
    * **class [im::floo::floolib::BMXUserProfile::MessageSetting](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile_1_1_message_setting.md)** <br>用户消息设置 
    * **class [im::floo::floolib::BMXUserService](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)** <br>用户Service 
    * **class [im::floo::floolib::BMXUserServiceListener](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md)** <br>用户状态监听者 
    * **class [im::floo::floolib::BMXVideoAttachment](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md)** <br>视频消息附件 
    * **class [im::floo::floolib::BMXVoiceAttachment](reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md)** <br>音频消息附件 
